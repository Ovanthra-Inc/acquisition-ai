---
name: Kinetic Executive
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#0051d5'
  on-secondary: '#ffffff'
  secondary-container: '#316bf3'
  on-secondary-container: '#fefcff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#002113'
  on-tertiary-container: '#009668'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#b4c5ff'
  on-secondary-fixed: '#00174b'
  on-secondary-fixed-variant: '#003ea8'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  metric-lg:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: 38px
    letterSpacing: -0.01em
  heading-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1440px
  sidebar-width: 260px
  gutter: 24px
  margin-page: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style

This design system is built on a foundation of **Corporate Modernism** with a focus on high-stakes reliability. The brand personality is authoritative yet frictionless, designed to evoke a sense of "quiet power" through automation. 

The visual strategy utilizes a high-contrast structural approach: a dark, commanding sidebar anchors the navigation, while the primary workspace remains airy and minimalist. This distinction helps users mentally separate "system controls" from "client data." The aesthetic avoids decorative flourishes, relying instead on precise alignment, generous whitespace, and a focused color application to guide the user's eye toward growth metrics and acquisition milestones.

## Colors

The color palette is engineered for professional trust and clear action hierarchy. 

- **Primary Branding:** Deep Navy (`#0F172A`) and Charcoal form the backbone of the identity, used for text and high-level navigation to provide a grounded feel.
- **Action Layer:** Vibrant Electric Blue (`#2563EB`) is reserved exclusively for primary CTAs and active interactive states, ensuring high discoverability.
- **Success States:** A dual-tone Green system distinguishes between 'Interested' (vibrant) and 'Closed' (deep) states, providing immediate positive reinforcement.
- **Backgrounds:** A clean Light Gray (`#F8FAFC`) workspace prevents eye fatigue during long sessions, contrasted by a high-contrast dark sidebar for structural clarity.

## Typography

The typography system leverages **Inter** for its exceptional legibility and systematic feel. The hierarchy is optimized for a data-dense SaaS environment:

- **Metrics:** Growth figures and KPIs use `metric-lg` with tight letter-spacing to emphasize magnitude.
- **Hierarchy:** Clear differentiation between `heading-md` for card titles and `label-caps` for secondary metadata ensures that users can scan complex tables and dashboards quickly.
- **Readability:** A baseline 16px font size for body copy ensures the platform feels accessible and professional, while 14px is utilized for dense data lists.

## Layout & Spacing

This design system utilizes a **Fixed-Fluid Hybrid Grid**. The sidebar remains fixed at 260px, while the main content area utilizes a 12-column fluid grid with a maximum cap of 1440px to prevent excessive line lengths on ultra-wide monitors.

A 4px baseline grid governs the rhythmic spacing:
- **Margins:** 32px outer page margins provide the "generous whitespace" required for a premium feel.
- **Gutters:** 24px spacing between cards ensures data sets feel distinct and organized.
- **Density:** Use `stack-lg` for separating major sections and `stack-sm` for internal card elements to maintain a clear information hierarchy.

## Elevation & Depth

Visual depth is achieved through **Tonal Layering** and **Ambient Shadows**. Instead of heavy shadows, this design system uses a "lifted" approach:

- **Surface 0 (Canvas):** The light gray background.
- **Surface 1 (Cards):** Pure white with a 1px border (`#E2E8F0`) and a very soft, diffused shadow (Offset: 0, 4px; Blur: 6px; Opacity: 0.05).
- **Surface 2 (Dropdowns/Modals):** Increased shadow depth (Offset: 0, 10px; Blur: 15px; Opacity: 0.1) to indicate temporary overlay.
- **Interactive Depth:** Buttons utilize a subtle 1px bottom-aligned inner shadow to feel tactile and clickable without appearing dated.

## Shapes

The shape language is defined by a **Medium Roundedness (8px)**. This radius is applied consistently to cards, input fields, and buttons. 

- **Standard Radius:** 8px for most containers to balance modern friendliness with professional rigor.
- **Large Radius:** 16px (`rounded-lg`) is reserved for decorative empty-state containers or large promotional banners.
- **Utility Shapes:** Status indicators (pills) use a fully rounded (pill-shaped) radius to distinguish them from interactive buttons.

## Components

- **Buttons:** Primary buttons are Electric Blue with white text. Secondary buttons use a Navy ghost-style (outline only). States should include a subtle darken on hover.
- **Cards:** All data is housed in 8px rounded white cards. Use a header section within cards separated by a light 1px border for titles and actions.
- **Input Fields:** Use a subtle gray background (`#F1F5F9`) with no border in their default state, transitioning to a white background with an Electric Blue border on focus.
- **Chips/Badges:** Use "Interested" and "Closed" badges with low-opacity background fills of their respective greens to keep the UI from feeling too loud.
- **Sidebar:** High-contrast Navy/Charcoal. Active states should use a left-aligned Electric Blue vertical accent bar (4px width).
- **Data Tables:** Row-based with no vertical borders; use subtle horizontal dividers. The first column (usually Client Name) should be semi-bold Navy to anchor the row.