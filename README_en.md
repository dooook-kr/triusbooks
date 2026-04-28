English | [한국어](./README.md)

# Trius Lounge Book List
A searchable catalog for the resident lounge at Gwangmyeong Trius.

## 1. Project Intent
Despite having thousands of books in our lounge, residents struggled to find specific titles because there was no way to search the collection. As my first toy project while learning AI-assisted programming, I developed this search page to solve this real-world inconvenience.

## 2. Features
* **Book Search:** Easily find books using keywords.
* **Target Audience:** Provides recommendations based on book content to help readers choose what to read.
* **Book Info Print/Capture:** Users can check book details and call numbers to print or capture on mobile. This makes finding physical books in the lounge much more efficient.

## 3. Strategic Approach
As a non-developer, I focused on building a system that is easy to update and maintain efficiently.
* **Simple Data Structure:** Used CSV format instead of a complex database, allowing anyone to update the list instantly using Excel or Notepad.
* **Agile Deployment:** Hosted via GitHub Pages to eliminate server costs and minimize long-term maintenance.
* **Scalability:** While currently focused on indexing, the structure is designed to support future features like reader reviews or visitor comments.

## 4. Tech Stack
Data processing and web visualization were implemented using the following tools:
* **Frontend:** HTML5, CSS3
* **Backend:** Python, Flask (for data processing)
* **Infrastructure:** GitHub Actions & Pages

## 5. Preview
Check out the live project here:  
[https://dooook-kr.github.io/triusbooks/](https://dooook-kr.github.io/triusbooks/)
