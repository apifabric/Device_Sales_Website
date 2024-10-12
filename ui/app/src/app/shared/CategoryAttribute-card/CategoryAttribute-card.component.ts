import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CategoryAttribute-card.component.html',
  styleUrls: ['./CategoryAttribute-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CategoryAttribute-card]': 'true'
  }
})

export class CategoryAttributeCardComponent {


}