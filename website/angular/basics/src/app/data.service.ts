import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Item {
  id: number;
  title: string;
}

@Injectable({
  providedIn: 'root'
})
export class DataService {

  private url = 'https://jsonplaceholder.typicode.com/posts';

  constructor(private http: HttpClient) { 
    console.log('Data service is activated!');
  }

  getItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.url);
  }
}
