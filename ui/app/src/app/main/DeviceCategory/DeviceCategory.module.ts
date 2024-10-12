import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {DEVICECATEGORY_MODULE_DECLARATIONS, DeviceCategoryRoutingModule} from  './DeviceCategory-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    DeviceCategoryRoutingModule
  ],
  declarations: DEVICECATEGORY_MODULE_DECLARATIONS,
  exports: DEVICECATEGORY_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class DeviceCategoryModule { }