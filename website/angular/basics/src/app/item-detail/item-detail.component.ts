import { Component } from '@angular/core';
import { DataService } from '../data.service';

interface Item {
  id: number;
  title: string;
}

@Component({
  selector: 'app-item-detail',
  standalone: true,
  imports: [ ],
  template: `<p>item-detail works!</p>

@if (item) {
  <div>
    <h2>Item Details</h2>
    <p>ID: {{ item.id }}</p>
    <p>Name: {{ item.title }}</p>
  </div>
}
@else {
    <ng-template #noDetails>
    <p>No details available.</p>
    </ng-template>
}

`,
  styleUrls: ['./item-detail.component.css']
})
export class ItemDetailComponent {
  item?: Item;

  constructor(private dataService: DataService) { 
    console.log('Item Detail Component is activated!');
  }

  ngOnInit() {
    // get  details from id given from parent and the service
    this.dataService.getItemById(1).subscribe((data: Item) => this.item = data)
    ;
  }
}
