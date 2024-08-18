import { Component, EventEmitter, Output } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { DataService } from '../data.service';

@Component({
  selector: 'app-item-search',
  standalone: true,
  imports: [FormsModule],
  template: `<p>item-search works!</p>
<input type="number" [(ngModel)]="itemid" placeholder="Enter item id" />
<button (click)="onSearch()">Search</button>
`,
  styleUrl: './item-search.component.css'
})
export class ItemSearchComponent {
  itemid: number | undefined;
  @Output() itemSearched = new EventEmitter<number>();
  item: any;

  constructor(private dataService: DataService) { 
    console.log('Item Search Component is activated!');
  }

  onSearch(): void {
    if (this.itemid !== null && this.itemid !== undefined) {
      console.log('searching for item', this.itemid);
      this.dataService.getItemById(this.itemid).subscribe((data: any) => {
        console.log('item found', data);
        this.item = data;
        this.itemSearched.emit(this.itemid);
      });
    }
  }
}
