< PROJECT ROOT >
   |—aigpt/
   |    |-- app/
   |    |    |-- __init__.py
   |    |    |
   |    |    |-- static/
   |    |    |    |-- css/
   |    |    |    |    |-- <CSS files>             # CSS files for styling
   |    |    |    |
   |    |    |    |-- js/
   |    |    |    |    |-- <JavaScript files>      # JavaScript files for interactive behavior
   |    |    |    |
   |    |    |    |-- images/
   |    |    |         |-- <image files>           # Image files used in the application
   |    |    |
   |    |    |-- templates/
   |    |    |    |
   |    |    |    |-- includes/
   |    |    |    |    |
   |    |    |    |    |-- navigation.html          # Top bar
   |    |    |    |    |-- sidebar.html             # Left sidebar
   |    |    |    |    |-- scripts.html             # JS scripts common to all pages
   |    |    |    |    |-- footer.html              # The common footer
   |    |    |    |
   |    |    |    |-- layouts/
   |    |    |    |    |
   |    |    |    |    |-- base.html                # Used by common pages like index, UI
   |    |    |    |    |-- base-fullscreen.html     # Used by auth pages (login, register)
   |    |    |    |
   |    |    |    |-- accounts/
   |    |    |    |    |
   |    |    |    |    |-- login.html               # Use layout `base-fullscreen.html`
   |    |    |    |    |-- register.html            # Use layout `base-fullscreen.html`
   |    |    |    |
   |    |    |    |-- index.html                    # The default page
   |    |    |    |-- page-404.html                 # Error 404 page (page not found)
   |    |    |    |-- page-500.html                 # Error 500 page (server error)
   |    |    |    |-- *.html                        # All other pages provided by the UI Kit
   |    |
   |    |-- requirements.txt
   |    |
   |    |-- run.py
   |
   |-- ************************************************************************
   |—education/
   |    |-- years/
   |    |    |-- 1st_year/
   |    |    |    |-- spring/
   |    |    |    |    |-- module1/
   |    |    |    |    |    |-- <module1_files>     # Files for module 1
   |    |    |    |    |
   |    |    |    |    |-- module2/
   |    |    |    |    |    |-- <module2_files>     # Files for module 2
   |    |    |    |    |
   |    |    |    |    |-- ...                      # Other modules in the spring season
   |    |    |    |
   |    |    |    |-- summer/
   |    |    |    |    |-- module1/
   |    |    |    |    |
