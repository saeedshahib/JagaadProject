# JagaadProject

 Jagaad | Senior Python Engineer - Test
Please read instructions carefully
Use this file as part of the README.md and share with us your project when you complete it.
Requirements
You want to collect stats about the messages your system processes.
For every customerId and for every type of message, you want to know how many messages have been processed and what is the total amount of that specific type for a date interval.
It follows the JSON Schema of the message:
{
    "$schema": "https://json-schema.org/draft/2019-09/schema",
    "$id": "http://jagaad.com/stats_message.json",
    "type": "object",
    "title": "Stats Message Schema",
    "required": [
        "customerId",
        "type",
        "amount",
        "uuid"
    ],
    "properties": {
        "customerId": {
            "type": "integer",
            "title": "The customerId is the customer unique identifier",
            "examples": [
1 ]
}, "type": {
            "type": "string",
            "default": "",
            "title": "The type of message received",
            "examples": [
"A" ]
        },
        "amount": {
            "type": "string",
            "title": "Amount billed to the customer, as a string with 3 decimals precision",
            "examples": [
"0.012" ]
},

         "uuid": {
            "type": "string",
            "title": "The message unique identifier",
            "examples": [
                "a596b362-08be-419f-8070-9c3055566e7c"
            ]
} },
    "examples": [{
        "customerId": 1,
        "type": "A",
        "amount": "0.012",
        "uuid": "a596b362-08be-419f-8070-9c3055566e7c"
}] }
Instructions
1. Write a REST API that will receive a single message and that updates a statistics table on a relational database.
2. Write a REST API that will provide statistical information back to the reader.
Hints
● use the python programming language, feel free to choose the best framework / libraries to get the task done
● no need to have a fully-working deployed environment, just a local working solution
● write tests
● write comments to facilitate reading for reviewers where code can be unclear
● use git and write well formed commit messages
● use of docker is appreciated

To run the project:
move to the root directory of project and run this command:
docker-compose up --build
