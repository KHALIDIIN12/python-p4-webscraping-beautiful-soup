from lib.scraper import get_courses, get_main_title


def test_get_courses():
    """Test that get_courses returns a list of course titles"""
    courses = get_courses()
    assert isinstance(courses, list)
    assert len(courses) > 0
    # Should contain expected course titles (check for any course-related content)
    assert any("Software Engineering" in course or "Course" in course for course in courses)


def test_get_main_title():
    """Test that get_main_title returns the main heading"""
    title = get_main_title()
    assert isinstance(title, str)
    assert len(title) > 0
    # Should return a non-empty string from the main heading
    assert "Bootcamp" in title or "Tech" in title or "Flatiron" in title

