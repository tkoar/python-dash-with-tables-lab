
# Dash with Tables Lab

## Introduction
In this lab we will practice creating data tables in Dash

## Objectives


## Getting Started with Dash

First things first, we will need to install all the parts of Dash that we will be using. We will need to pip install:
    * dash -- *dash's backend*
    * dash-renderer -- *dash's front-end*
    * dash-html-components -- *dash's components for creating HTML layouts and tags on the web page*
    * dash-core-components -- *dash's components for creating data visualizations and other tools*
    * plotly -- *the plotly graphing library*
    
We can install all of these by simpling running one command in our terminal:
    
> `pip install dash dash-renderer dash-html-components dash-core-components plotly`

## Setting Up a Dash App

To create a new Dash Application, we need to first define our imports in our `app.py` file, which will be the following:

```python
import dash # importing the dash framework
import dash_core_components as dcc # importing the core components from dash
import dash_html_components as html # importing the html components from dash
```

Once we have our imports set-up, we can create a new instance of a Dash app with the following line of code:

```python
# creating a new instance of Dash
app = dash.Dash() 

# telling our app to start the server if we are running this file
if __name__ == '__main__':
    app.run_server(debug=True)
```

Okay, once we've done the above, we have ourselves a Dash app! It doesnt do much (or show much in our browser), but we can certainly run the server and look at in our browser. Let's try it by running the following command in our terminal and then opening a new tab in our browser and navigating to `http://localhost:8050/`

> `python app.py`

Uh oh! We got an error; `AttributeError: 'NoneType' object has no attribute 'traverse'`. Dash is expecting some html, specifically a layout, to display, but we haven't yet given it a layout. Let's keep going and fix this issue.

## Creating a Layout in a Dash App

Okay, we have our Dash app almost working. Let's see how we add a layout to our app. 

You may have already guessed at this point but it is as simple as:

```python
app.layout = # some code
```

Unfortunately, we can't just assign the layout to some HTML or even a string of HTML, we need to use dash's html components. So, since we imported the dash_html_components as html, we will reference it as such. To start, we will assign the layout to an html element. Usually we will chose a `div` to start. 

```python
app.layout = html.Div("Hello World")
```

Now, if we add this in directly underneath where we instantiated our dash app, we will be able to successfully start our dash app's server and again visit it in the browser at `http://localhost:8050/`. Try it out!

Great! We see a div with the text "Hello World". Since we will be adding more than just a simple div to our page, we should re-format this layout a bit. Instead of giving our layout's most outer div tag just a string of "Hello World", we give it a `children` attribute and assign it to a list. 

```python
app.layout = html.Div(children=[])
```

> **Note:** You can give any dash html element a children attribute, however, you should only do this if you are nesting multiple html elements within that element (i.e. our page layout, an ordered or unordered list of elements, etc.)

Inside this list we are going to add all the other html elements we want to display on our page. Let's add an `h1` tag that reads "Hello, this is my first dash app" and below that let's add a `p` tag that reads "Still under construction... :)". 

> **Note:** as our layout grows, it is important to have a clean formatting so that we can more easily read and manage our code base. Below is an illustration of how we should format the dash html elements in our list of html children.

```python
app.layout = html.Div(children=[
    html.ExampleElement("Example Text"),
    html.AnotherElement("More text")
])
```

Now, when we visit our app in the browser, we should see a page that looks like this:

> <h1>Hello, this is my first dash app</h1>
> <p>Still under construction... :)</p>

## Adding Data Visualization With Graphs

Okay okay, we can display HTML. That is fun and all but let's get to the good stuff and get some cool graphs on the page already!

Remember when we imported dash's core components? Well, we are going to finally use them! We will use the `dcc` import to create a graph. To do this, we will simply add a third element to our list of children in our app's outer most `div`. 

Creating a graph with dash's core components is very similar to creating a graph using the plotly libray. First we will create a new graph object with `dcc.Graph()`. The graph object takes a few different attributes. Below we see an example graph object:

> ```python
dcc.Graph(
    id = "Example Graph",
    figure = {
        data: [
            {'x': [1,2,3], 'y': [4,5,6], 'type': "bar", 'name': "Example"},
            {'x': [3,2,1], 'y': [6,5,4], 'type': "line", 'name': "Another Example"}
        ],
        layout: {
            'title': "Example Graph"
        }
    }
```

As we can see, first our graph has an `id` attribute. Although we wont be using the ID in this lab, this is a necessary attribute. Next, our graph has a dictionary called `figure`, which has two attributes, `data` and `layout`. Data, is the stuff we want to plot on our graph -- it has data points for the `x` and `y` axes as well as the type of graph  and the name of each grouping of data. The figure's layout arrtibute takes a title so we can give our graph a descriptive title -- pretty simple.

Let's try building this out with the data we already have provided for us in the uber_data.py file. We can either import this data or copy it over to our app.py file. Let's give our graph an `id` of "uber_data_" we have our data in place, we will give our graph the title, `"Uber Pricing in Brooklyn and Manhattan"` and then our graph should be good to go! Let's save our work and view our dash app in the browser again.

![preview of new dash app](https://learn-verified.s3.amazonaws.com/data-science-assets/dash_manhattan_brooklyn_uber_prices.png)

## Summary

Great work! In this lab we practiced setting up a dash app. We then added a layout using dash's html components and learned how to create nested html tags on our layout. Finally we practiced data visualisation using dash's core components to create a graph with pre-polutated data showing the relationship between distance and price in taxi fares in Brooklyn and Manhattan.
