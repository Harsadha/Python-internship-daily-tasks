# MINI PROJECT- DAILY SALES REPORT AUTOMATION- W3D5
'''
✓ Read sales data from a JSON file
✓ Calculate: total sales, top 5 products, department summary
✓ Generate an HTML formatted report
✓ Send HTML email + CSV attachment via SMTP to multiple recipients
✓ Use ThreadPoolExecutor to send emails concurrently
✓ Decorate key functions with @timer and @logger
✓ Log everything to automation.log
✓ Push complete project to GitHub with a proper PR'''

import json
import csv
import logging

from collections import defaultdict

from concurrent.futures import ThreadPoolExecutor
from decorators import (logger, timer)
from email_sender import send_email

logging.basicConfig(filename="automation.log", level=logging.INFO,
    format=("%(asctime)s- %(levelname)s - %(message)s"))

@timer
@logger
def load_sales_data(file_path):
    with open(file_path,"r") as file:
        return json.load(file)

@timer
@logger
def calculate_total_sales(data):
    return sum(item["quantity"] *item["price"]for item in data)

@timer
@logger
def get_top_products(data):
    revenue = defaultdict(float)
    for item in data:
        revenue[item["product"]] += (item["quantity"]* item["price"])
    return sorted( revenue.items(),key=lambda x: x[1],reverse=True)[:5]

@timer
@logger
def get_department_summary(data):
    summary = defaultdict(float)
    for item in data:
        summary[item["department"]] += (item["quantity"]* item["price"])
    return dict(summary)

@timer
@logger
def generate_csv(summary):
    csv_file = "sales_summary.csv"
    with open(csv_file,"w",newline="",encoding="utf-8") as file:
        writer = csv.writer(file) 
        writer.writerow( ["Department","Sales"])
        for dept, sales in summary.items():
            writer.writerow([dept,sales])
    return csv_file

@timer
@logger
def generate_html_report(total_sales,top_products,department_summary):
    html = f"""
    <html>
    <body>

    <h1>Sales Report</h1>

    <h2>Total Sales</h2>
    <p>Rs. {total_sales}</p>

    <h2>Top 5 Products</h2>

    <ul>
    """
    for product, revenue in top_products:
        html += (f"<li>{product} - Rs. {revenue}</li>")

    html += "</ul>"
    html += """
    <h2>Department Summary</h2>

    <table border='1' cellpadding='5'>
    <tr>
        <th>Department</th>
        <th>Sales</th>
    </tr>
    """
    for dept, sales in department_summary.items():
        html += f"""
        <tr>
            <td>{dept}</td>
            <td>₹ {sales}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    with open("report.html","w",encoding="utf-8") as file:
        file.write(html)
    return html

@timer
@logger
def send_reports(recipients,html_content,csv_file):
    with ThreadPoolExecutor( max_workers=5) as executor:
        executor.map(lambda recipient:send_email(recipient,html_content,csv_file), recipients)


def main():

    logging.info( "Automation Started")
    data = load_sales_data("sales_data.json")
    total_sales = (calculate_total_sales(data))
    top_products = ( get_top_products(data))

    department_summary = (get_department_summary(data))
    csv_file = generate_csv(department_summary)

    html_content = (generate_html_report( total_sales,top_products,department_summary))
    recipients = [
        "h.ranjeeth.kumar@accenture.com",
        "harsadha.r05@gmail.com",
        "harsadha2310312@ssn.edu.in"
    ]

    send_reports( recipients,html_content,csv_file)
    logging.info("Automation Completed")

    print( "Report Generated Successfully")


if __name__ == "__main__":
    main()