# Whisper - AI Usage and Prompts

## Overview
The Whisper backend was created with assistance from Claude (Anthropic). Below are the key prompts and decisions.

## Model Used
Claude Haiku 4.5 and Github Copilot GPT-6 Luna

## Backend Prompts
for my 15113 class, this is hte next assignemtn:

Goal: Build a simple backend service on Render.com and integrate it with your portfolio website or a GitHub Pages site. This assignment teaches you how to build server-side code that handles operations that are better done on the backend (like using APIs securely, storing data, or processing user input).
Why This Matters: Many features are best implemented on the backend because: (1) you can keep API keys and secrets secure, (2) you can process and store data safely, (3) you can do computationally intensive work, and (4) you can validate user input before using it. This assignment teaches you to identify when a backend is useful and how to build one quickly using AI.
Examples of what you might build:

* A chatbot on your website that talks to an AI (e.g., a character version of yourself or a famous person) using OpenAI or Claude API
* A form that saves data to a database
* A page that fetches data from an API that requires authentication
* A tool that processes user input in some way (e.g., translates text, generates images, analyzes sentiment)

what is a good idea thats interesting that i could put on my website? and then should i use vercel or render?

do you have any more ideas that are more interesrting and fun?

any less technical and more creative ideas?

so i was researching adn found "Personal Content API (Headless CMS): Build your own micro-blog or project portfolio service that serves structured JSON data to your static front end. [[1](https://roadmap.sh/backend/project-ideas), [2](https://www.quora.com/What-kind-of-projects-should-I-make-to-show-my-back-end-in-web-development-as-a-junior-for-my-portfolio)]" and is this similar to my current websiteblog on vercel or no? and then i dont know if any of the suggestions are really speaking to me so far

ok i think the memory weaver/moodboard is cool if its done right, like those reels where people give good life lessons as anoniymous messages i think thats pretty interesting

wait so i made the folder locally and added the code in vscode, what do i do now? is it different from what i normally do, which is creating github repo and then doing terminal comand line stuff to connect it

is this important An environment file is configured but terminal environment injection is disabled. Enable "python.terminal.useEnvFile" to 
 wait before i make this change, what is this doing? i want it to be a place to leave a message kinda like a message book but idk if i want too much ai to change what ithe quotes say?

let's create a new repo for the frontend. i want it to be simple for now and we can revamp later, but something like a bulletin board would be cute? more ideas? and then make sure that since render is on free tier, we want to try and write something that tells us that the render is waking up (e..g a skeleton loader or a message loader): Makes requests to your backend using fetch() or another HTTP client

* Displays the responses nicely (or provides confirmation that the request was handled)
* Handles errors (e.g., if the backend is down or the user provides bad input)


wait i think jar wolud be cool, and you can gt them out the jar
i think something simple for now but maybe in the future it can be like dumping the papers into the jar?
is this too complicated? we can have it simpler for now

yes! should i make a new folder too on vscode and then new repo

cant peek inside. also should i start siwthcing to copilot now i like doing frontend with github copilot? is there any other logistical things i need to do now other than frontned design?

done with front end and its pushed to github! now readme, can you make it pretty simple.m "Write a clear README explaining what your backend does, how to run it locally, how the frontend calls it, and where secrets are stored."

* What your backend does (what endpoints it has, what parameters it accepts, what it returns)
* How the frontend communicates with the backend (which endpoints it calls, when, and what it does with the response)
* How to set up and run the backend (including any environment variables or API keys needed locally)
* How authentication or secrets are handled (e.g., API keys stored on the backend, not in frontend code)


and then can you explain what render specificlaly is? I know how it seems to work and what backend vs front end is but i dont undersatnd why you nee to keep them separate repos

## Frontend Prompts
ask any clarifying questions before we begin. so we have the frontned of a whisper leaving messsages in a jar thing. please make it look more reaistic and interesting, and rae the bugs in the photo becuase oof frontend or backend? we can fix backend later.


can you remove:
A few words, held gently

A quiet place to let go

Made for the things that are hard to say.
01 / LET IT GO
02 / TAKE A MOMENT
and the border is messed up in photo.

yay it works now! anyways, is there any way to make this more interactve? other than just people leaving different messages (like this is just a comment section). just give ideas

ooh yes can we do draw one note instead of show all of them