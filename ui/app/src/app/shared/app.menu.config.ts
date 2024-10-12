import { MenuRootItem } from 'ontimize-web-ngx';

import { AccessoryCardComponent } from './Accessory-card/Accessory-card.component';

import { CategoryAttributeCardComponent } from './CategoryAttribute-card/CategoryAttribute-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { DeviceCategoryCardComponent } from './DeviceCategory-card/DeviceCategory-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderItemCardComponent } from './OrderItem-card/OrderItem-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { PromotionCardComponent } from './Promotion-card/Promotion-card.component';

import { ReviewCardComponent } from './Review-card/Review-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';

import { SupplierProductCardComponent } from './SupplierProduct-card/SupplierProduct-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Accessory', name: 'ACCESSORY', icon: 'view_list', route: '/main/Accessory' }
    
        ,{ id: 'CategoryAttribute', name: 'CATEGORYATTRIBUTE', icon: 'view_list', route: '/main/CategoryAttribute' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'DeviceCategory', name: 'DEVICECATEGORY', icon: 'view_list', route: '/main/DeviceCategory' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderItem', name: 'ORDERITEM', icon: 'view_list', route: '/main/OrderItem' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Promotion', name: 'PROMOTION', icon: 'view_list', route: '/main/Promotion' }
    
        ,{ id: 'Review', name: 'REVIEW', icon: 'view_list', route: '/main/Review' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
        ,{ id: 'SupplierProduct', name: 'SUPPLIERPRODUCT', icon: 'view_list', route: '/main/SupplierProduct' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AccessoryCardComponent

    ,CategoryAttributeCardComponent

    ,CustomerCardComponent

    ,DeviceCategoryCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderItemCardComponent

    ,ProductCardComponent

    ,PromotionCardComponent

    ,ReviewCardComponent

    ,SupplierCardComponent

    ,SupplierProductCardComponent

];