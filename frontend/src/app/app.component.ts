import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NgFor } from '@angular/common';
import { Chart } from 'chart.js/auto';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [NgFor],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent implements OnInit {
  items: any[] = [];
  mongoItems: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get<any[]>('http://localhost:8000/api/items/').subscribe(data => {
      this.items = data;
      this.renderChart();
    });
    this.http.get<any[]>('http://localhost:8000/api/mongo-items/').subscribe(data => this.mongoItems = data);
  }

  renderChart(): void {
    new Chart('itemChart', {
      type: 'bar',
      data: {
        labels: this.items.map(i => i.name),
        datasets: [{ label: 'Quantity', data: this.items.map(i => i.quantity) }]
      }
    });
  }
}
