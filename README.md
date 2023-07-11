# todo

## Features
1. authenticated users can get tasks
2. authenticated users can crud tasks 
3. authenticated users can be categorized
2. authenticated users can crud category

## Tables
1. Category
2. Task

## Schema
User:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| username | str  | unique username |
| password | str  | password |

Category:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| user | str  | name |
| name | str  | name_category |

Tasks:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| user | fk  | name        |
| cotegory | fk | cotegory_name |
| description | str  | description   |
| title | str  | task   |
| complated | bool  | like and dislike   |
