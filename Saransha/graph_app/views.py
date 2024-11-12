# graph_app/views.py
import pandas as pd
import matplotlib.pyplot as plt
import io
import urllib, base64
from django.shortcuts import render
import matplotlib


def dynamic_graph_view(request):


    # First Graph: Journal and Conference Count by Author
    data = {
        'Main Author': ['Dr. Shrinivas R. Zanwar', 'Dr. Saroj Date', 'Dr. Ulhas B Shinde'],
        'Journal': [8, 2, 21],
        'Conference': [1, 1, 3]
    }
    df = pd.DataFrame(data)
    
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    bar_width = 0.35
    index = range(len(df['Main Author']))
    
    ax1.bar(index, df['Journal'], bar_width, label='Journal', color='blue')
    ax1.bar([i + bar_width for i in index], df['Conference'], bar_width, label='Conference', color='orange')
    
    ax1.set_xlabel('Main Author')
    ax1.set_ylabel('Count')
    ax1.set_title('Journal and Conference Count by Author')
    ax1.set_xticks([i + bar_width / 2 for i in index])
    ax1.set_xticklabels(df['Main Author'], rotation=45, ha='right')
    ax1.legend()
    
    buf1 = io.BytesIO()
    plt.savefig(buf1, format='png')
    buf1.seek(0)
    graph1 = base64.b64encode(buf1.getvalue()).decode('utf-8')
    buf1.close()
    
    # Second Graph: Publications by Author Over Time
    years = ['2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
    publications = {
        "Dr. Saroj Date": [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2],
        "Dr. Shrinivas R. Zanwar": [0, 0, 2, 0, 0, 1, 1, 0, 0, 2, 1],
        "Dr. Ulhas B Shinde": [2, 4, 3, 0, 2, 0, 5, 7, 0, 1, 2],
    }

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    bar_width = 0.25
    index = range(len(years))

    for i, (author, counts) in enumerate(publications.items()):
        ax2.bar([x + i * bar_width for x in index], counts, bar_width, label=author)

    ax2.set_xlabel('Year')
    ax2.set_ylabel('Number of Publications')
    ax2.set_title('Publications by Author Over Time')
    ax2.set_xticks([x + bar_width for x in index])
    ax2.set_xticklabels(years, rotation=45, ha='right')
    ax2.legend()

    buf2 = io.BytesIO()
    plt.savefig(buf2, format='png')
    buf2.seek(0)
    graph2 = base64.b64encode(buf2.getvalue()).decode('utf-8')
    buf2.close()

    data = {
        'Main Author': ['Dr. Saroj Date', 'Dr. Shrinivas R. Zanwar', 'Dr. Ulhas B Shinde'],
        'Titles': [5, 12, 38]
    }
    
    # Convert data to DataFrame
    df = pd.DataFrame(data)
    
    # Plotting the bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df['Main Author'], df['Titles'], color='steelblue')
    
    # Customizing the chart
    ax.set_xlabel('Main Author')
    ax.set_ylabel('Number of Titles')
    ax.set_title('Publication Count by Author')
    plt.xticks(rotation=45, ha='right')

    # Save the plot to a string buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_png = buf.getvalue()
    buf.close()
    
    # Encode the image to a base64 string
    graph3 = base64.b64encode(image_png).decode('utf-8')
    buf1.close()
    

    return render(request, 'graph_app/dynamic_graph.html', {'graph1': graph1, 'graph2': graph2,'graph3': graph3})

       
    
