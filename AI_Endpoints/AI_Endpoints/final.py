from diffusers import DiffusionPipeline
import torch
import os
from PIL import Image
import torch
from diffusers import StableDiffusionImg2ImgPipeline
from tts import audiog
from argparse import Namespace
from SadTalker.inference import main


def text2img(prompt,output_path):
    base = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, variant="fp16", use_safetensors=True
    )
    base.to("cuda")
    refiner = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-xl-refiner-1.0",
        text_encoder_2=base.text_encoder_2,
        vae=base.vae,
        torch_dtype=torch.float16,
        use_safetensors=True,
        variant="fp16",
    )
    refiner.to("cuda")

    # Define how many steps and what % of steps to be run on each experts (80/20) here
    n_steps = 40
    high_noise_frac = 0.8

    # run both experts
    image = base(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_end=high_noise_frac,
        output_type="latent",
    ).images
    image = refiner(
        prompt=prompt,
        num_inference_steps=n_steps,
        denoising_start=high_noise_frac,
        image=image,
    ).images[0].save(output_path)

def img2img(url,output_path):
    pipe = AutoPipelineForImage2Image.from_pretrained(
        "Lykon/dreamshaper-7",
        torch_dtype=torch.float16,
        variant="fp16",
    ).to("cuda")

    # set scheduler
    pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)

    # load LCM-LoRA
    pipe.load_lora_weights("latent-consistency/lcm-lora-sdv1-5")

    # prepare image
    url = url
    init_image = load_image(url)


    prompt = "full body, realistic detailed 3d avatar with nice human facial features, life like expression, realistic skin tone, facial details and expressions, light condition for accurate representation 16:9"

    # pass prompt and image to pipeline
    generator = torch.manual_seed(0)
    image = pipe(
        prompt,
        image=init_image,
        num_inference_steps=4,
        guidance_scale=1,
        strength=0.6,
        generator=generator
    ).images[0].save(output_path)

def tts_gen(text, output_file_name, voice="daniel"):
    audiog.tts_aud(text, output_file_name, voice)


def run_main(driven_audio, source_image, ref_eyeblink, ref_pose, checkpoint_dir, result_dir, pose_style, batch_size,
             size, expression_scale, input_yaw, input_pitch, input_roll, enhancer, background_enhancer, cpu, 
             face3dvis, still, preprocess, verbose, old_version, net_recon, init_path, use_last_fc, 
             bfm_folder, bfm_model, focal, center, camera_d, z_near, z_far):
    args_dict = {
        "driven_audio": driven_audio,
        "source_image": source_image,
        "ref_eyeblink": ref_eyeblink,
        "ref_pose": ref_pose,
        "checkpoint_dir": checkpoint_dir,
        "result_dir": result_dir,
        "pose_style": pose_style,
        "batch_size": batch_size,
        "size": size,
        "expression_scale": expression_scale,
        "input_yaw": input_yaw,
        "input_pitch": input_pitch,
        "input_roll": input_roll,
        "enhancer": enhancer,
        "background_enhancer": background_enhancer,
        "cpu": cpu,
        "face3dvis": face3dvis,
        "still": still,
        "preprocess": preprocess,
        "verbose": verbose,
        "old_version": old_version,
        "net_recon": net_recon,
        "init_path": init_path,
        "use_last_fc": use_last_fc,
        "bfm_folder": bfm_folder,
        "bfm_model": bfm_model,
        "focal": focal,
        "center": center,
        "camera_d": camera_d,
        "z_near": z_near,
        "z_far": z_far,
    }

    args = Namespace(**args_dict)
    main(args)