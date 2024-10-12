import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'DeviceCategory-new',
  templateUrl: './DeviceCategory-new.component.html',
  styleUrls: ['./DeviceCategory-new.component.scss']
})
export class DeviceCategoryNewComponent {
  @ViewChild("DeviceCategoryForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}