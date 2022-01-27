# Newsletter-Subscription-Platform

## Run the code using Linux Terminal
```
$ python3 main.py
```

## Problem Statement

You have come up with an idea to build a newsletter subscription platform. Users can subscribe to monthly newsletters on your platform.

We have 3 entities:

1. User: id, name, email
2. Newsletter: id, category_id, title, user_id, price
3. Category: id, name

* Register user API:

Allow users to register on the platform. They should be able to register on the platform using their name and email.

```
Sample request: { "name": "John Doe", "email": "john.doe@wonderfulemail.com" }
Sample response: { "user_id": 1 }
```

* Create newsletter API:

Any user on this platform should be able to publish a newsletter. Each newsletter is part of one or more categories. Newsletters are either free-to-subscribe ( in which case the price is 0 INR ) or pay-to-subscribe ( in which case the user decides the price ). 

```
Sample request: { "title" : "Latest in tech by John Doe", "user_id": 1, "price" : 10, "categories": [ "technology" , "latest", "science" ] }
Sample response: { "newsletter_id" : 1}
```

The category should be automatically created if it doesn't exist already.

* Get newsletters API:

Any user should be able to query the newsletters on this platform using categories.

```
Sample request: { "categories" : [ "science", "technology"] }
Sample response: {"newsletters":[{"science":[{"newsletter_id":1,"title":"Latest in tech by John Doe"},{"newsletter_id":2,"title":"Old in science by John Doe"}]},{"technology":[{"newsletter_id":1,"title":"Latest in tech by John Doe"}]}]}

{
  "newsletters": [
    {
      "science": [
        {
          "newsletter_id": 1,
          "title": "Latest in tech by John Doe"
        },
        {
          "newsletter_id": 2,
          "title": "Old in science by John Doe"
        }
      ]
    },
    {
      "technology": [
        {
          "newsletter_id": 1,
          "title": "Latest in tech by John Doe"
        }
      ]
    }
  ]
}
```

* Subscribe to newsletter API:

Any user on this platform should be able to subscribe to any newsletter. The platform only provides a monthly subscription option.

```
Sample request: {"newsletter_id":1,"subscriber_user_id":2}
Sample response: {"subscription_id": 1}

key: user_id
Value : Array of all the newsletter_id

 {"newsletter_id":1,"subscriber_user_id":3}
  {"newsletter_id":1,"subscriber_user_id":4}
  
  earnings: 30 user_id: 1 
```

* Fetch earnings API:

All users who have created a newsletter should be able to retrieve their monthly earnings for the current month

```
Sample request: { "user_id" : 1}
Sample response: { "earnings": 10}
```



## Guidelines

Write 1-2 sample unit test cases - no need to be exhaustive - but the ones that are written should be production quality.

Use an external or in-memory database.

Try to be as close as possible to production quality coding conventions

Handle failures wherever applicable

Since time is limited, please prioritize tasks in the order they have been mentioned in the problem.

We are not building this for scale. We are also not assessing the choice of the tech stack, so anything that you are comfortable with is fine.
