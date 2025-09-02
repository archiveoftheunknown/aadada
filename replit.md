# Overview

This is a static website displaying the official Indonesian government suspension notice for blocked websites, as issued by the Ministry of Communication and Digital Affairs (Kementerian Komunikasi dan Digital). The site serves as a standard blocking page that informs users when they attempt to access content that has been suspended by the Indonesian government due to containing prohibited content types such as pornography, online gambling, fraud, hate speech, or intellectual property violations.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The application uses a purely static approach with no backend components:

- **Technology Stack**: Pure HTML5 with Tailwind CSS for styling
- **Design Pattern**: Single-page static website with responsive mobile-first design
- **Styling Framework**: Tailwind CSS loaded via CDN for rapid development and consistent design
- **Typography**: Google Fonts (Inter family) for professional appearance
- **Responsive Design**: Mobile-first approach using Tailwind's responsive utilities

## Content Structure
- **Language**: Indonesian (id locale) as the primary target audience
- **Accessibility**: Semantic HTML structure with proper ARIA attributes
- **SEO Optimization**: Comprehensive meta tags including Open Graph and Twitter Card support
- **Print Support**: Print-friendly styling for document archiving

## Performance Optimizations
- **External Dependencies**: Minimal external resources (Tailwind CDN, Google Fonts)
- **Image Loading**: Optimized image handling with responsive sizing
- **Font Loading**: Optimized font loading with display=swap parameter
- **Smooth Scrolling**: Enhanced user experience with CSS scroll-behavior

## Deployment Strategy
- **Platform**: Designed specifically for GitHub Pages deployment
- **Entry Point**: Single index.html file serving as the main page
- **Static Hosting**: No server-side processing required, purely client-side rendering

# External Dependencies

## CDN Services
- **Tailwind CSS**: https://cdn.tailwindcss.com - CSS framework for styling
- **Google Fonts**: fonts.googleapis.com - Inter font family for typography

## Asset Sources
- **Government Logo**: Wikipedia Commons - Official Indonesian Ministry logo
- **Icons**: Inline SVG icons for content categorization (no external icon library dependency)

## Browser Support
- All modern browsers with CSS3 and HTML5 support
- Mobile browsers with responsive viewport support
- Print media support for document generation

# Platform-Specific Behavior

## GitHub Pages
- **404.html**: Custom redirect page that shows when accessing non-existent paths
- Redirects all random URLs to the main page using JavaScript
- Shows "Mengarahkan ke halaman utama..." with spinner before redirecting
- Works within GitHub Pages static hosting limitations

## Local Development (Replit)
- **server.py**: Python server that handles redirects server-side
- Provides more robust redirect handling for development
- All paths redirect to main page with proper HTTP 301 redirects