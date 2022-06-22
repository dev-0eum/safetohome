# Safe to Home

## outline 

* Purpose
    * To navigate to user's home safely

## pseudo code
```c
/*
1. Get the user's current location. (Start point)
2. Get the user's home location. (End point)
3. Find the patches* btw two points.
4. Import CCTV coordinate data in each patches.
5. Make each coordinate nodes.
6. Cost is btw each nodes' distances.
7. Setting route to navigate using dijstra algorithm.

*The patch is arbitraily made by developer to divide sections

*/
```


* Point to note
    * to run this promgram we need website has domain
    * (cuz of to assign api key from Kakao)