def test_cases(number):
    return testCases[number]


testCases = [
    # [severity, description]
    ['Blocker', 'when user goes to main page, page should be loaded'],
    ['Blocker', 'In Home page, when user search "Iphone 12" button, he should see result for Iphone 12'],
    ['Blocker', 'In Home page, when user click "Sing up" button, he should see Sign up Page'],
    ['Blocker', 'In Home page, when user click "Sing in" button, he should see Sign in Page'],
    ['Blocker', 'In Home page, when user click "Careers" button, he should see Careers Page'],
    ['Blocker', 'In Home Page, when user search "Iphone 12" button, After clicking on the product, he should see Detail Page'],
    ['Blocker', 'In Register Page, when user register with a empty user, he should see Error Message'],
    ['Blocker', 'In Register Page, when user register with a empty user, he should see Error Message'],
    ['Blocker', 'In Detail Page, when user click "Add to Cart" button, he should see Cart Page'],
    ['Blocker', "In Detail Page, when user click 'Buy Now' button, he should see Login Page if you haven't logged in yet"],
    ['Blocker', "In Careers Page, when user search 'Software' and 'Canada' address button, he should see search results Careers Page"],
    ['Blocker', "In Job Page, when user click 'Apply Now' button, he should see Apply Page"],


]
