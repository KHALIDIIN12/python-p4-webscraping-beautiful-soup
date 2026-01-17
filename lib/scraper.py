from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}


def get_courses():
    """Scrape course titles from Flatiron School's courses page"""
    html = requests.get("https://flatironschool.com/our-courses/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    course_list = []
    
    # Find courses in list items that are direct navigation items
    for li in doc.find_all('li'):
        text = li.get_text(strip=True)
        # Filter for main course categories (short, meaningful names)
        known_courses = [
            'Software Engineering',
            'Data Science', 
            'Product Design',
            'Cybersecurity',
            'Game Design',
            'Game Programming',
            'AI & Machine Learning'
        ]
        if text in known_courses:
            course_list.append(text)
    
    return course_list


def get_main_title():
    """Scrape the main title from Flatiron School's homepage"""
    html = requests.get("https://flatironschool.com/", headers=headers)
    doc = BeautifulSoup(html.text, 'html.parser')
    
    # Look for h1 elements first
    h1_elements = doc.select('h1')
    for h1 in h1_elements:
        if h1.contents:
            text = h1.contents[0].strip()
            if text and len(text) > 10:
                return text
    
    # Fallback: try to get any significant text from the page
    title_element = doc.select('.heading-financier')
    if title_element and title_element[0].contents:
        return title_element[0].contents[0].strip()
    
    # Try meta title as last resort
    meta_title = doc.select('title')
    if meta_title and meta_title[0].contents:
        return meta_title[0].contents[0].strip()
    
    return None

