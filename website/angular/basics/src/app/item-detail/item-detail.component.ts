import { Component, Input, SimpleChanges, OnChanges, OnInit, OnDestroy } from '@angular/core';
import { NgIf } from '@angular/common';
import { DataService } from '../data.service';
import { Subject } from 'rxjs';
import { takeUntil } from 'rxjs/operators';

interface Item {
  id: number;
  title: string;
}

@Component({
  selector: 'app-item-detail',
  standalone: true,
  imports: [ NgIf ],
  template: `
    <ng-container *ngIf="item; else noItem">
      <div>
        <h3>Item Detail</h3>
        <p>Item ID: {{ item.id }}</p>

      </div>
    </ng-container>
    <ng-template #noItem>
      <div>
        <p>No item selected</p>
      </div>
    </ng-template>
  `,
  styleUrls: ['./item-detail.component.css']
})
export class ItemDetailComponent implements OnChanges, OnInit, OnDestroy {
  @Input() item: Item | undefined;
  private unsubscribe$ = new Subject<void>();

  constructor(private dataService: DataService) { 
    console.log('Item Detail Component - item:', this.item);
  }

  ngOnInit() {
    this.fetchItemDetails();
  }

  ngOnChanges(changes: SimpleChanges) {
    console.log('ItemDetailComponent - ngOnChanges', changes);
    if (changes['item'] && changes['item'].currentValue) {
      this.fetchItemDetails();
    }
  }

  ngOnDestroy() {
    this.unsubscribe$.next();
    this.unsubscribe$.complete();
  }

  private fetchItemDetails() {
    if (this.item) {
      this.dataService.getItemById(this.item.id)
        .pipe(takeUntil(this.unsubscribe$))
        .subscribe({
          next: (data: Item) => this.item = data,
          error: (error) => console.error('Error fetching item details:', error)
        });
    }
    else {
      console.log('ItemDetailComponent - item is undefined');
    }
  }
}