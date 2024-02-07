
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#task1
# def highScoreMov():
#     num = int(input())
#     if movies[num]["imdb"] > 5.5:
#         return True
#     else:
#         return False

# res = highScoreMov()
# print(res)

#task2
# def highScoreMov():
#     a = []
#     for i in range(len(movies)):
#         if movies[i]["imdb"] > 5.5:
#             a.append(movies[i]["name"])
            
#     print(a)
# highScoreMov()

#task3
# def categ():
#     a = []
#     x = input()
#     for i in range(len(movies)):
#         if movies[i]["category"] == x:
#             a.append(movies[i]["name"])
#     print(a)
# categ()

#task4
# def imdbAvg():
#     imdb = 0
#     for i in range(len(movies)):
#         imdb += movies[i]["imdb"]
#     avg = imdb / len(movies)
#     print(avg)

# imdbAvg()

#task5
# def categ():
#     a = 0
#     x = input()
#     for i in range(len(movies)):
#         if movies[i]["category"] == x:
#             a += movies[i]["imdb"]
#     print(a)
# categ()
