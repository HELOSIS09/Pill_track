<div align="center">

# 📈 Progress Calendar

**A drag-and-drop habit tracker with a built-in notepad, styled like the PyCharm IDE.**

![HTML](https://img.shields.io/badge/HTML-CSS-JavaScript-a8d600?style=flat-square)
![No dependencies](https://img.shields.io/badge/dependencies-none-4dd0e1?style=flat-square)
![Storage](https://img.shields.io/badge/data-stays%20in%20your%20browser-ff6b9a?style=flat-square)

</div>

---

## 🌱 Why I built this

I wanted one simple place to see, at a glance, **what I actually did each day**: workouts, study sessions, and any other habit I decide to track.

Most habit apps felt either too heavy (accounts, subscriptions, notifications) or too plain (a single checkbox per day). I wanted something I could open, drop a coloured pill on a date, and instantly see my month. I also spend a lot of time in PyCharm, so I gave the whole thing the same dark teal look, which makes it feel like a tool I already use.

The goals were:

1. **See progress honestly.** Every day card shows exactly which habits were done, so there is nowhere to hide.
2. **Keep a notepad next to it.** Reflections and plans belong beside the calendar, not in another app.
3. **Keep it mine.** No sign-up, no server, no tracking. Everything stays on my device.
4. **Learn by building.** This is a small personal project made to practise front-end work.

> **Transparency:** this project was built with help from an AI assistant (Claude), based on my requirements and iterations. I direct what it does and how it looks; the code was written collaboratively.

---

## ✨ Features

### 📅 Calendar (`calendar.py` tab)
- Create habit "pills" with a name and a colour (12 colours to choose from).
- **Drag a pill onto any date**, or drag it between dates to move it.
- On touch screens: tap a pill to select it, then tap dates to place it.
- Large day cards that show every habit on that day, plus a done count such as `2/3`.
- Click a day to open its details: tick habits on or off and add a short note that appears on the card.
- Days where every habit is done get a green highlight.

### 📝 Notepad (`notes.md` tab)
- Multiple notes, each with an editable title.
- Line numbers and a monospace editor, like an IDE.
- **Point-wise writing:** type `- ` for bullets, and Enter continues the list. Press Enter on an empty bullet to end it.
- Numbered lists, `# Heading` and `## Heading`, `` `code` `` and `**bold**`.
- Checklists with `- [ ]`. Tick them in the live preview and the note updates.
- Tab indents a sub-point; sub-bullets get different colours.
- Toolbar buttons for Bullet, Todo, numbered list, headings and indent.
- **Autosaves**, so your notes are still there after you close the page.

### 📊 Stats (`stats.py` tab)
- Percentage of active days this month.
- Habits logged this month and days with progress in the last 30 days.
- Current and best streak for every habit.
- Bar chart for the last 7 days and a 17-week heatmap.

### 💾 Backup
- The **Backup** button shows all your data as text. Copy it to export, paste it to import on another device.

---

## 🚀 How to use

1. Open `index.html` in any modern browser (or the hosted link, if you have one).
2. Add a habit in the left panel and pick a colour.
3. Drag it onto the days you did it.
4. Click a day to add a note. Open **notes.md** for longer writing.
5. Check **stats.py** to see your streaks.

No build step, no install. It is a single HTML file.

---

## 🧰 Built with

- Plain **HTML, CSS and JavaScript** in one file
- Your browser's `localStorage` for saving
- System monospace fonts (nothing is downloaded)

---

## ⚠️ Honest limitations

- **Data lives only in one browser on one device.** Clearing site data, or switching browser or phone, means starting empty unless you use Backup first.
- **No automatic sync** and no accounts. Moving data is manual copy and paste.
- A habit can be placed **once per day**; it records done or not done, not how much.
- Backups are text you copy yourself, so remember to make one now and then.
- Not tested on every browser and device. It is designed for current Chrome, Edge, Firefox and Safari, and may have rough edges.
- Mobile works, but the layout is a simplified version of the desktop one.

---

## 🛣️ Ideas for later

These are ideas only, not promises:

- Download and upload backup files
- Weekly goals per habit
- Optional sync between devices
- Light theme and more IDE colour schemes

---

## 👤 Author

Made by **Apurva Swarnkaar**, a hospitality and tourism student who likes building small tools that make daily work easier.

## 📄 License

Choose a license for the repository (for example MIT) and add it here.

<div align="center">

*Small steps, tracked honestly.* 🌿

</div>
