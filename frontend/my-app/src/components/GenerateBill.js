import React from 'react';
import { jsPDF } from 'jspdf';

const GenerateBill = () => {
  const billData = {
    billNumber: '12345',
    date: '2024-11-14',
    customerName: 'John Doe',
    items: [
      { description: 'Product 1', quantity: 2, price: 50, total: 100 },
      { description: 'Product 2', quantity: 1, price: 150, total: 150 },
      { description: 'Product 3', quantity: 3, price: 30, total: 90 },
    ],
    totalAmount: 340,
  };

  const generatePDF = () => {
    const doc = new jsPDF();
    
    // Title of the bill
    doc.setFontSize(20);
    doc.text('Invoice Bill', 20, 20);

    // Bill Number and Date
    doc.setFontSize(12);
    doc.text(`Bill Number: ${billData.billNumber}`, 20, 30);
    doc.text(`Date: ${billData.date}`, 150, 30);
    
    // Customer Name
    doc.text(`Customer: ${billData.customerName}`, 20, 40);
    
    // Table Headers
    const headers = ['Description', 'Quantity', 'Price', 'Total'];
    let yPosition = 50;
    doc.text(headers[0], 20, yPosition);
    doc.text(headers[1], 80, yPosition);
    doc.text(headers[2], 120, yPosition);
    doc.text(headers[3], 160, yPosition);
    
    // Draw table of items
    billData.items.forEach((item, index) => {
      yPosition += 10;
      doc.text(item.description, 20, yPosition);
      doc.text(item.quantity.toString(), 80, yPosition);
      doc.text(`$${item.price}`, 120, yPosition);
      doc.text(`$${item.total}`, 160, yPosition);
    });

    // Total Amount
    yPosition += 20;
    doc.text(`Total Amount: $${billData.totalAmount}`, 120, yPosition);

    // Save the PDF
    doc.save(`Bill-${billData.billNumber}.pdf`);
  };

  return (
    <div>
      <h1>Generate Bill</h1>
      <button onClick={generatePDF}>Download Bill as PDF</button>
    </div>
  );
};

export default GenerateBill;
