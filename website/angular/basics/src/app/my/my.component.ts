import { Component  } from '@angular/core';
import { DataService } from '../data.service';

interface Item {
  id: number;
  title: string;
}

@Component({
  selector: 'app-my',
  standalone: true,
  imports: [],
  template: `
    {{ items.length }} items found.

    @for(item of items; track item.id) {
      <div>{{ item.id }} - {{ item.title }}</div>
    }
  `,
  styleUrl: './my.component.css'
})
export class MyComponent {
  items: Item[] = [];

  constructor(private dataService: DataService) { }

  ngOnInit() {
    this.dataService.getItems().subscribe((data: Item[]) => this.items = data);
  }
}
