## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Wanderkarm/Coursera-Test/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Wanderkarm/Coursera-Test/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.

### Scheduled ChatGPT Usage

A new script `scheduled_chatgpt.py` lets you run ChatGPT prompts automatically. The script uses the `openai` and `schedule` packages.

Example usage to run daily at 9 AM:

```bash
python scheduled_chatgpt.py "Hello, world" --daily --time 09:00
```

Replace the prompt with your own text. Set `OPENAI_API_KEY` in your environment to authenticate with OpenAI.

For a weekly run on Mondays at 8 AM:

```bash
python scheduled_chatgpt.py "Weekly report" --weekly monday --time 08:00
```

The script will keep running, checking the schedule every second. Use cron or a process manager to run it in the background.
