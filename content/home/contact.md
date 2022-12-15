---
# An instance of the Contact widget.
widget: contact

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 130

title: Contact
subtitle: Let's get in touch

content:
  # Automatically link email and phone or display as text?
  autolink: true

  # Email form provider
  form:
    provider: netlify
    formspree:
      id:
    netlify:
      # Enable CAPTCHA challenge to reduce spam?
      captcha: false

  # Contact details (edit or remove options as required)
  email: titimbo@caltech.edu
  phone: ''
  address:
    street: 1200 E California Blvd
    city: Pasadena
    region: CA
    postcode: '91125'
    country: United States
    country_code: US
  coordinates:
    latitude: '37.4275'
    longitude: '-122.1697'
  directions: Keck Building, Office 209
  # office_hours:
  #   - 'Monday 10:00 to 13:00'
  #   - 'Wednesday 09:00 to 10:00'
  # appointment_url: 'https://calendly.com'
  contact_links:
    # - icon: twitter
    #   icon_pack: fab
    #   name: DM Me
    #   link: 'https://twitter.com/Twitter'
    # - icon: video
    #   icon_pack: fas
    #   name: Zoom Me
    #   link: 'https://zoom.com'
    - icon: skype
      icon_pack: fab
      name: Skype Me
      link: 'https://zoom.com'

design:
  columns: '2'
---
