import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MyComponent } from './my/my.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, MyComponent],
  template: `
    <h1>{{ title }}</h1>
    <app-my></app-my>
    <hr>
  `,
  styleUrl: './app.component.css'
})
  
export class AppComponent {
  title = 'basics';
}
