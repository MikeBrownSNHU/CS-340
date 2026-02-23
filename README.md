# CS-340 Dashboard Project Reflection

## Writing Maintainable, Readable, and Adaptable Programs

When I write programs, I try to think about the next person who might have to read or update my code — even if that person is just me a few months later. Keeping things organized and separating responsibilities makes a big difference. In this project, the CRUD Python module I built in Project One really helped with that.

Instead of putting database queries directly into the dashboard code, I kept all database operations inside the CRUD module. That made the dashboard code cleaner and easier to follow. If something needs to change in the database connection or query logic, I only have to update it in one place. That saves time and reduces the chance of breaking something else.

Another benefit is reusability. The CRUD module isn’t tied only to this dashboard. I could reuse it in another project that connects to MongoDB, whether that’s another dashboard, a reporting script, or even a small web service. Building things in a modular way makes future projects easier and faster to develop.

## My Approach as a Computer Scientist

For this project, I approached it like I would a real client request. I started by carefully reviewing what Grazioso Salvare needed. Then I broke the work into smaller steps: connect to the database, retrieve the data correctly, build the data table, create the map visualization, and finally make everything interactive.

This project felt different from earlier assignments because it brought everything together. I wasn’t just writing a query or just building a UI — I had to think about how the database, Python code, and dashboard all worked together as one system. It required more planning and testing along the way.

In the future, I would follow the same process:
- Understand the requirements first  
- Design the database structure carefully  
- Keep backend logic separate from the interface  
- Test small pieces before combining them  

Taking this structured approach makes complex projects more manageable and reduces mistakes.

## What Computer Scientists Do and Why It Matters

Computer scientists solve problems by building systems that manage and interpret data. In this project, the goal wasn’t just to store animal shelter data — it was to make it easier to understand and use.

By building the dashboard, I created a tool that helps users filter data, view trends, and make decisions more efficiently. Instead of manually sorting through raw records, staff members can quickly interact with the data in a visual way.

Projects like this show why computer science matters. Well-designed systems help organizations work smarter, save time, and make better decisions based on data. Even something as simple as organizing information properly can have a big impact on how effectively a company operates.
