import React from 'react'

export default function Fab() {
  return (
    <button class="floatingButtonWrap">
        <div class="floatingButtonInner">
            <a href="#" class="floatingButton">
                <i class="fa fa-plus icon-default"></i>
            </a>
            <ul class="floatingMenu">
                <li>
                    <a href="#">Add Supplier</a>
                </li>
                <li>
                    <a href="#">Add Table</a>
                </li>
                <li>
                    <a href="#">Add Food</a>
                </li>
                <li>
                    <a href="#">Add Menu Type</a>
                </li>
                <li>
                    <a href="#">Add Menu</a>
                </li>
                <li>
                    <a href="https://google.com" target="_blank">Go To Google</a>
                </li>
                <li>
                    <a href="#">Add Inventory</a>
                </li>
                <li>
                    <a href="#">Add Staff</a>
                </li>
            </ul>
        </div>
    </button>
  )
}
