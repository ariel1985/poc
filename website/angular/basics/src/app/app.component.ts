import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MyComponent } from './my/my.component';
import { ItemDetailComponent } from './item-detail/item-detail.component';
import { ItemSearchComponent } from './item-search/item-search.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MyComponent, ItemDetailComponent, ItemSearchComponent],
  template: `
    <h1>{{ title }} App</h1>

    <h2>Item Search Component</h2>
    <app-item-search></app-item-search>
    
    <h2>Item Detail Component</h2>
    <app-item-detail></app-item-detail>
    
    <h2>My List Component</h2>
    <app-my></app-my>
    <hr>
  `,
  styleUrl: './app.component.css'
})
  
export class AppComponent {
  title = 'basics';
}
