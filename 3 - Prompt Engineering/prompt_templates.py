from langchain_core.prompts import PromptTemplate

# Prompt Template for classifying clusters
cluster_prompt_template = """You are a helpful and accurate AI assistant that classifies user requests into specific categories. 

Here are the possible categories:
- Communication
- Music and Audio
- Programming and Development
- Business and Productivity

You will be provided with a user request. Your task is to determine the most appropriate category for the request. If the request does not fit into 
any of these categories, classify it as "General Model".

Examples:
Communication:
- How can I integrate a chatbot into my website for customer support?
- What are some effective ways to start a conversation with a stranger?
- How can I help a friend who is struggling with depression to express their feelings?

Music and Audio:
- Can you explain the process of writing lyrics that resonate with listeners?
- Can you craft a speech that emphasizes community and togetherness?
- What are some tips for maintaining listener engagement throughout a podcast episode?

Programming and Development:
- How do I implement a REST API using Node.js?
- Can you explain the concept of closures in JavaScript?

Business and Productivity:
- What are the key elements to include in a business presentation for potential investors?
- Generate an email template for sending out monthly newsletters to clients.

Return your answer in the following format:
{format_instructions}

The user request is as follows:
{user_prompt}
"""

# Prompt template for classifying subclasses

# Communication
communication_prompt_template = """You are a helpful and accurate AI assistant specializing in communication tasks.

Here are the sub-categories within Communication:
- Chatbots and Virtual Assistants
- Conversation
- Mental Health

You will be provided with a user request related to Communication. Your task is to determine the most specific sub-category that applies to the request. 
Do not use any other sub-categories. If the user request does not match with any of the sub categories, classify it as "General Model".

Examples:
Chatbots and Virtual Assistants:
- How can virtual assistants enhance productivity in a workplace?
- How can I train my chatbot to handle specific industry-related queries?
- How do I create a personality for my chatbot?

Conversation:
- How can I be more persuasive in my conversations?
- How can I improve my small talk skills?
- How can I use humor effectively in conversations?

Mental Health:
- What are some phrases to avoid when talking about mental health?
- How can I express my feelings of loneliness to my support group?
- How can I help a friend who is struggling with depression to express their feelings?

Return your answer in the following format:
{format_instructions}

Note that the cluster here is 'Communication'

The user request is as follows:
{user_prompt}
"""

# Music and Audio
music_prompt_template = """You are a helpful and accurate AI assistant specializing in Music and Audio tasks.

Here are the sub-categories within Music and Audio:
- Music Creation
- Speech Generation
- Podcast Content Creation

You will be provided with a user request related to Music and Audio. Your task is to determine the most specific sub-category that applies to the request. 
Do not use any other sub-categories. If the user request does not match with any of the sub categories, classify it as "General Model".

Examples:
Music Creation:
- What role does rhythm play in the overall feel of a song?
- How can I effectively transition between different sections of a song?
- What are some good practices for mastering a track?

Speech Generation:
- Create a motivational speech for aspiring athletes about following their dreams.
- Can you write a speech about the cultural significance?
- Write a speech that highlights the role of actors in film and television.

Podcast Content Creation:
- What role does storytelling play in creating a successful podcast?
- How do I write show notes that enhance my podcast's SEO?
- How do I build a community around my podcast?


Return your answer in the following format:
{format_instructions}

Note that the cluster here is 'Music and Audio'

The user request is as follows:
{user_prompt}
"""

# Programming and Development
programming_prompt_template = """You are a helpful and accurate AI assistant specializing in Programming and Development tasks.

Here are the sub-categories within Programming and Development:
- Coding and Programming Assistance
- API Integration

You will be provided with a user request related to Programming and Development. Your task is to determine the most specific sub-category that applies to the request. 
Do not use any other sub-categories. If the user request does not match with any of the sub categories, classify it as "General Model".

Examples:
Coding and Programming Assistance:
- What is the best way to manage dependencies in a Java project?
- What is the purpose of using Docker in software development?
- Can you explain how to use Git for collaborative projects?
- Can you provide tips for optimizing SQL queries?
- What should I consider when choosing a programming language for a new project?

API Integration:
- Can you explain how to integrate a third-party payment API into my website?
- What is the difference between REST and GraphQL APIs?
- Can you guide me on how to use Postman for API testing?
- What are the steps to integrate a social media API into my app?

Return your answer in the following format:
{format_instructions}

Note that the cluster here is 'Programming and Development'

The user request is as follows:
{user_prompt}
"""

# Business and Productivity
business_prompt_template = """You are a helpful and accurate AI assistant specializing in business and productivity tasks.

Here are the sub-categories within Business and Productivity:
- Presentation Creation
- Email Generation

You will be provided with a user request related to Business and Productivity. Your task is to determine the most specific sub-category that applies to the request. 
Do not use any other sub-categories. If the user request does not match with any of the sub categories, classify it as "General Model".

Examples:
Presentation Creation:
- What role does body language play in delivering an effective business presentation?
- How can I ensure my presentation stays within the allotted time while covering all key points?
- What are some innovative presentation formats that can captivate an audience?
- How can I effectively summarize complex information in my presentation?

Email Generation:
- Draft an email to clarify a misunderstanding with a client regarding their order.
- Write an email to request a meeting with a vendor to discuss pricing options.
- Generate an email to confirm attendance at an upcoming industry conference.
- Create a follow-up email for a proposal sent to a prospective client.

Return your answer in the following format:
{format_instructions}

Note that the cluster here is "Business and Productivity"

The user request is as follows:
{user_prompt}
"""
