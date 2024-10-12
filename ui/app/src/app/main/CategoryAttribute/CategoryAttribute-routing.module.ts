import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CategoryAttributeHomeComponent } from './home/CategoryAttribute-home.component';
import { CategoryAttributeNewComponent } from './new/CategoryAttribute-new.component';
import { CategoryAttributeDetailComponent } from './detail/CategoryAttribute-detail.component';

const routes: Routes = [
  {path: '', component: CategoryAttributeHomeComponent},
  { path: 'new', component: CategoryAttributeNewComponent },
  { path: ':id', component: CategoryAttributeDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CategoryAttribute-detail-permissions'
      }
    }
  }
];

export const CATEGORYATTRIBUTE_MODULE_DECLARATIONS = [
    CategoryAttributeHomeComponent,
    CategoryAttributeNewComponent,
    CategoryAttributeDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CategoryAttributeRoutingModule { }