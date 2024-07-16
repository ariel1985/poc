import { Component, Input } from '@angular/core';

interface Item {
  id: number;
  title: string;
}

@Component({
  selector: 'app-item-detail',
  templateUrl: './item-detail.component.html',
  styleUrls: ['./item-detail.component.css']
})
export class ItemDetailComponent {
  @Input() item: Item | null = null;
}
