import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CategoryAttribute-new',
  templateUrl: './CategoryAttribute-new.component.html',
  styleUrls: ['./CategoryAttribute-new.component.scss']
})
export class CategoryAttributeNewComponent {
  @ViewChild("CategoryAttributeForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}