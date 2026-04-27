# KC SpotifyAnalyzer

## Pages

### Home

---

## Layout Structure

### Header
- Left: Logo (click → redirects to `/`)
- Center: Title
- Right: Account settings (user menu / dropdown)

---

### Sidebar (Groups)
- Vertical list of Groups
- Each Group is a circular button (React component)

#### Rules:
- Only ONE group can be selected at a time
- There is a special "Global Group"
    - Represents all data combined
    - Always available
- Other groups represent user-defined or filtered datasets

#### Behavior:
- Clicking a group:
    - deselects previous group
    - sets active group state globally
- Active group affects all analytics in Main Section

---

### Main Section
- (to be defined later)
- Will display analytics based on selected Group

---

### Footer
- Copyright text
- App version (e.g. v1.0.0)
- GitHub link