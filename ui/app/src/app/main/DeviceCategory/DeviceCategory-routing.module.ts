import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DeviceCategoryHomeComponent } from './home/DeviceCategory-home.component';
import { DeviceCategoryNewComponent } from './new/DeviceCategory-new.component';
import { DeviceCategoryDetailComponent } from './detail/DeviceCategory-detail.component';

const routes: Routes = [
  {path: '', component: DeviceCategoryHomeComponent},
  { path: 'new', component: DeviceCategoryNewComponent },
  { path: ':id', component: DeviceCategoryDetailComponent,
    data: {
      oPermission: {
        permissionId: 'DeviceCategory-detail-permissions'
      }
    }
  },{
    path: ':category_id/CategoryAttribute', loadChildren: () => import('../CategoryAttribute/CategoryAttribute.module').then(m => m.CategoryAttributeModule),
    data: {
        oPermission: {
            permissionId: 'CategoryAttribute-detail-permissions'
        }
    }
},{
    path: ':category_id/Product', loadChildren: () => import('../Product/Product.module').then(m => m.ProductModule),
    data: {
        oPermission: {
            permissionId: 'Product-detail-permissions'
        }
    }
}
];

export const DEVICECATEGORY_MODULE_DECLARATIONS = [
    DeviceCategoryHomeComponent,
    DeviceCategoryNewComponent,
    DeviceCategoryDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class DeviceCategoryRoutingModule { }