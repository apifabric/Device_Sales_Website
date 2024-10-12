import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './DeviceCategory-card.component.html',
  styleUrls: ['./DeviceCategory-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.DeviceCategory-card]': 'true'
  }
})

export class DeviceCategoryCardComponent {


}