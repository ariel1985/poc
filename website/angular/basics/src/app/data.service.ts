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

  // private url = 'https://jsonplaceholder.typicode.com/posts';
  private url = 'http://localhost:3000/repos';

  constructor(private http: HttpClient) { 
    console.log('Data service is activated!');
  }

  getItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.url);
  }

  getItemById(id: number): Observable<Item> {
    return this.http.get<Item>(`${this.url}/${id}`);
  }
}
