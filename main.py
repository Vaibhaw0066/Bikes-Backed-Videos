import time
import traceback

import requests
import json
import os

from dotenv import load_dotenv
import downloadYoutubeVideo
from logs import getLogger
import  logging

load_dotenv()

logger = getLogger()
failed_model_ids = dict()

TOKEN_DEV = os.getenv("TOKEN_DEV") # TOKEN_DEV
DEV = "https://cms-bike-backend.qac24svc.dev"


TOKEN_PROD = os.getenv("TOKEN_PROD")
PROD = "https://cms-bike-backend-prod.cars24.team"

serverType = "prod" # "dev"

video_id_lst =  [
            {
                "videoid": 1188,
                "model_id": 1399
            },
            {
                "videoid": 1232,
                "model_id": 1399
            },
            {
                "videoid": 1430,
                "model_id": 1399
            },
            {
                "videoid": 1436,
                "model_id": 1399
            },
            {
                "videoid": 1730,
                "model_id": 1399
            },
            {
                "videoid": 1774,
                "model_id": 1399
            },
            {
                "videoid": 1821,
                "model_id": 1399
            },
            {
                "videoid": 2068,
                "model_id": 1399
            },
            {
                "videoid": 2108,
                "model_id": 1399
            },
            {
                "videoid": 2273,
                "model_id": 1399
            },
            {
                "videoid": 2372,
                "model_id": 1399
            },
            {
                "videoid": 2630,
                "model_id": 1399
            },
            {
                "videoid": 2989,
                "model_id": 1399
            },
            {
                "videoid": 2990,
                "model_id": 1399
            },
            {
                "videoid": 2992,
                "model_id": 1399
            },
            {
                "videoid": 3443,
                "model_id": 1399
            },
            {
                "videoid": 3612,
                "model_id": 1399
            },
            {
                "videoid": 4110,
                "model_id": 1399
            },
            {
                "videoid": 4145,
                "model_id": 1399
            },
            {
                "videoid": 4146,
                "model_id": 1399
            },
            {
                "videoid": 4221,
                "model_id": 1399
            },
            {
                "videoid": 4246,
                "model_id": 1399
            },
            {
                "videoid": 1464,
                "model_id": 1404
            },
            {
                "videoid": 1761,
                "model_id": 1404
            },
            {
                "videoid": 1805,
                "model_id": 1404
            },
            {
                "videoid": 1837,
                "model_id": 1404
            },
            {
                "videoid": 2078,
                "model_id": 1404
            },
            {
                "videoid": 2181,
                "model_id": 1404
            },
            {
                "videoid": 2275,
                "model_id": 1404
            },
            {
                "videoid": 2358,
                "model_id": 1404
            },
            {
                "videoid": 2474,
                "model_id": 1404
            },
            {
                "videoid": 2666,
                "model_id": 1404
            },
            {
                "videoid": 2827,
                "model_id": 1404
            },
            {
                "videoid": 3128,
                "model_id": 1404
            },
            {
                "videoid": 3181,
                "model_id": 1404
            },
            {
                "videoid": 3211,
                "model_id": 1404
            },
            {
                "videoid": 3724,
                "model_id": 1404
            },
            {
                "videoid": 3952,
                "model_id": 1404
            },
            {
                "videoid": 3960,
                "model_id": 1404
            },
            {
                "videoid": 3964,
                "model_id": 1404
            },
            {
                "videoid": 3966,
                "model_id": 1404
            },
            {
                "videoid": 3971,
                "model_id": 1404
            },
            {
                "videoid": 3979,
                "model_id": 1404
            },
            {
                "videoid": 3982,
                "model_id": 1404
            },
            {
                "videoid": 3994,
                "model_id": 1404
            },
            {
                "videoid": 4000,
                "model_id": 1404
            },
            {
                "videoid": 4011,
                "model_id": 1404
            },
            {
                "videoid": 4013,
                "model_id": 1404
            },
            {
                "videoid": 4027,
                "model_id": 1404
            },
            {
                "videoid": 4033,
                "model_id": 1404
            },
            {
                "videoid": 4035,
                "model_id": 1404
            },
            {
                "videoid": 4037,
                "model_id": 1404
            },
            {
                "videoid": 1243,
                "model_id": 1124
            },
            {
                "videoid": 1489,
                "model_id": 1124
            },
            {
                "videoid": 1547,
                "model_id": 1124
            },
            {
                "videoid": 1908,
                "model_id": 1124
            },
            {
                "videoid": 1909,
                "model_id": 1124
            },
            {
                "videoid": 2049,
                "model_id": 1124
            },
            {
                "videoid": 2090,
                "model_id": 1124
            },
            {
                "videoid": 2268,
                "model_id": 1124
            },
            {
                "videoid": 2388,
                "model_id": 1124
            },
            {
                "videoid": 2477,
                "model_id": 1124
            },
            {
                "videoid": 2576,
                "model_id": 1124
            },
            {
                "videoid": 2859,
                "model_id": 1124
            },
            {
                "videoid": 2876,
                "model_id": 1124
            },
            {
                "videoid": 2892,
                "model_id": 1124
            },
            {
                "videoid": 3196,
                "model_id": 1124
            },
            {
                "videoid": 3371,
                "model_id": 1124
            },
            {
                "videoid": 3534,
                "model_id": 1124
            },
            {
                "videoid": 3667,
                "model_id": 1124
            },
            {
                "videoid": 3717,
                "model_id": 1124
            },
            {
                "videoid": 4076,
                "model_id": 1124
            },
            {
                "videoid": 4114,
                "model_id": 1124
            },
            {
                "videoid": 4132,
                "model_id": 1124
            },
            {
                "videoid": 4165,
                "model_id": 1124
            },
            {
                "videoid": 4166,
                "model_id": 1124
            },
            {
                "videoid": 4217,
                "model_id": 1124
            },
            {
                "videoid": 4219,
                "model_id": 1124
            },
            {
                "videoid": 4235,
                "model_id": 1124
            },
            {
                "videoid": 4245,
                "model_id": 1124
            },
            {
                "videoid": 4258,
                "model_id": 1124
            },
            {
                "videoid": 1197,
                "model_id": 1297
            },
            {
                "videoid": 1212,
                "model_id": 1297
            },
            {
                "videoid": 1446,
                "model_id": 1297
            },
            {
                "videoid": 1492,
                "model_id": 1297
            },
            {
                "videoid": 1831,
                "model_id": 1297
            },
            {
                "videoid": 1906,
                "model_id": 1297
            },
            {
                "videoid": 2120,
                "model_id": 1297
            },
            {
                "videoid": 2291,
                "model_id": 1297
            },
            {
                "videoid": 2357,
                "model_id": 1297
            },
            {
                "videoid": 2368,
                "model_id": 1297
            },
            {
                "videoid": 2387,
                "model_id": 1297
            },
            {
                "videoid": 2741,
                "model_id": 1297
            },
            {
                "videoid": 2800,
                "model_id": 1297
            },
            {
                "videoid": 3120,
                "model_id": 1297
            },
            {
                "videoid": 3271,
                "model_id": 1297
            },
            {
                "videoid": 1247,
                "model_id": 1125
            },
            {
                "videoid": 1755,
                "model_id": 1125
            },
            {
                "videoid": 2008,
                "model_id": 1125
            },
            {
                "videoid": 2041,
                "model_id": 1125
            },
            {
                "videoid": 2074,
                "model_id": 1125
            },
            {
                "videoid": 2173,
                "model_id": 1125
            },
            {
                "videoid": 2251,
                "model_id": 1125
            },
            {
                "videoid": 2297,
                "model_id": 1125
            },
            {
                "videoid": 2360,
                "model_id": 1125
            },
            {
                "videoid": 2394,
                "model_id": 1125
            },
            {
                "videoid": 2470,
                "model_id": 1125
            },
            {
                "videoid": 2735,
                "model_id": 1125
            },
            {
                "videoid": 2904,
                "model_id": 1125
            },
            {
                "videoid": 3021,
                "model_id": 1125
            },
            {
                "videoid": 3093,
                "model_id": 1125
            },
            {
                "videoid": 3366,
                "model_id": 1125
            },
            {
                "videoid": 3503,
                "model_id": 1125
            },
            {
                "videoid": 3527,
                "model_id": 1125
            },
            {
                "videoid": 3682,
                "model_id": 1125
            },
            {
                "videoid": 3950,
                "model_id": 1125
            },
            {
                "videoid": 3953,
                "model_id": 1125
            },
            {
                "videoid": 3955,
                "model_id": 1125
            },
            {
                "videoid": 3968,
                "model_id": 1125
            },
            {
                "videoid": 3976,
                "model_id": 1125
            },
            {
                "videoid": 3981,
                "model_id": 1125
            },
            {
                "videoid": 3998,
                "model_id": 1125
            },
            {
                "videoid": 3999,
                "model_id": 1125
            },
            {
                "videoid": 4003,
                "model_id": 1125
            },
            {
                "videoid": 4012,
                "model_id": 1125
            },
            {
                "videoid": 4021,
                "model_id": 1125
            },
            {
                "videoid": 4028,
                "model_id": 1125
            },
            {
                "videoid": 4032,
                "model_id": 1125
            },
            {
                "videoid": 4036,
                "model_id": 1125
            },
            {
                "videoid": 4044,
                "model_id": 1125
            },
            {
                "videoid": 1374,
                "model_id": 1195
            },
            {
                "videoid": 1435,
                "model_id": 1195
            },
            {
                "videoid": 1530,
                "model_id": 1195
            },
            {
                "videoid": 1824,
                "model_id": 1195
            },
            {
                "videoid": 2037,
                "model_id": 1195
            },
            {
                "videoid": 2211,
                "model_id": 1195
            },
            {
                "videoid": 2256,
                "model_id": 1195
            },
            {
                "videoid": 2606,
                "model_id": 1195
            },
            {
                "videoid": 2632,
                "model_id": 1195
            },
            {
                "videoid": 2844,
                "model_id": 1195
            },
            {
                "videoid": 2848,
                "model_id": 1195
            },
            {
                "videoid": 3018,
                "model_id": 1195
            },
            {
                "videoid": 3075,
                "model_id": 1195
            },
            {
                "videoid": 3307,
                "model_id": 1195
            },
            {
                "videoid": 3308,
                "model_id": 1195
            },
            {
                "videoid": 3407,
                "model_id": 1195
            },
            {
                "videoid": 3413,
                "model_id": 1195
            },
            {
                "videoid": 3455,
                "model_id": 1195
            },
            {
                "videoid": 3556,
                "model_id": 1195
            },
            {
                "videoid": 3648,
                "model_id": 1195
            },
            {
                "videoid": 3702,
                "model_id": 1195
            },
            {
                "videoid": 1344,
                "model_id": 1345
            },
            {
                "videoid": 1478,
                "model_id": 1345
            },
            {
                "videoid": 1485,
                "model_id": 1345
            },
            {
                "videoid": 1502,
                "model_id": 1345
            },
            {
                "videoid": 1739,
                "model_id": 1345
            },
            {
                "videoid": 1922,
                "model_id": 1345
            },
            {
                "videoid": 1991,
                "model_id": 1345
            },
            {
                "videoid": 2023,
                "model_id": 1345
            },
            {
                "videoid": 2099,
                "model_id": 1345
            },
            {
                "videoid": 2383,
                "model_id": 1345
            },
            {
                "videoid": 2843,
                "model_id": 1345
            },
            {
                "videoid": 2854,
                "model_id": 1345
            },
            {
                "videoid": 3214,
                "model_id": 1345
            },
            {
                "videoid": 3269,
                "model_id": 1345
            },
            {
                "videoid": 3278,
                "model_id": 1345
            },
            {
                "videoid": 3390,
                "model_id": 1345
            },
            {
                "videoid": 3691,
                "model_id": 1345
            },
            {
                "videoid": 1476,
                "model_id": 1123
            },
            {
                "videoid": 1711,
                "model_id": 1123
            },
            {
                "videoid": 1722,
                "model_id": 1123
            },
            {
                "videoid": 1782,
                "model_id": 1123
            },
            {
                "videoid": 1979,
                "model_id": 1123
            },
            {
                "videoid": 2056,
                "model_id": 1123
            },
            {
                "videoid": 2363,
                "model_id": 1123
            },
            {
                "videoid": 2366,
                "model_id": 1123
            },
            {
                "videoid": 2475,
                "model_id": 1123
            },
            {
                "videoid": 2561,
                "model_id": 1123
            },
            {
                "videoid": 2572,
                "model_id": 1123
            },
            {
                "videoid": 2661,
                "model_id": 1123
            },
            {
                "videoid": 2814,
                "model_id": 1123
            },
            {
                "videoid": 3145,
                "model_id": 1123
            },
            {
                "videoid": 3275,
                "model_id": 1123
            },
            {
                "videoid": 3438,
                "model_id": 1123
            },
            {
                "videoid": 3630,
                "model_id": 1123
            },
            {
                "videoid": 4074,
                "model_id": 1123
            },
            {
                "videoid": 4109,
                "model_id": 1123
            },
            {
                "videoid": 4153,
                "model_id": 1123
            },
            {
                "videoid": 4156,
                "model_id": 1123
            },
            {
                "videoid": 4174,
                "model_id": 1123
            },
            {
                "videoid": 4212,
                "model_id": 1123
            },
            {
                "videoid": 4244,
                "model_id": 1123
            },
            {
                "videoid": 1211,
                "model_id": 1090
            },
            {
                "videoid": 1601,
                "model_id": 1090
            },
            {
                "videoid": 2013,
                "model_id": 1090
            },
            {
                "videoid": 2166,
                "model_id": 1090
            },
            {
                "videoid": 2282,
                "model_id": 1090
            },
            {
                "videoid": 2289,
                "model_id": 1090
            },
            {
                "videoid": 2453,
                "model_id": 1090
            },
            {
                "videoid": 2650,
                "model_id": 1090
            },
            {
                "videoid": 2729,
                "model_id": 1090
            },
            {
                "videoid": 2731,
                "model_id": 1090
            },
            {
                "videoid": 2811,
                "model_id": 1090
            },
            {
                "videoid": 2855,
                "model_id": 1090
            },
            {
                "videoid": 2857,
                "model_id": 1090
            },
            {
                "videoid": 2888,
                "model_id": 1090
            },
            {
                "videoid": 3257,
                "model_id": 1090
            },
            {
                "videoid": 3368,
                "model_id": 1090
            },
            {
                "videoid": 3430,
                "model_id": 1090
            },
            {
                "videoid": 3473,
                "model_id": 1090
            },
            {
                "videoid": 3483,
                "model_id": 1090
            },
            {
                "videoid": 3537,
                "model_id": 1090
            },
            {
                "videoid": 3572,
                "model_id": 1090
            },
            {
                "videoid": 3583,
                "model_id": 1090
            },
            {
                "videoid": 3662,
                "model_id": 1090
            },
            {
                "videoid": 3669,
                "model_id": 1090
            },
            {
                "videoid": 3718,
                "model_id": 1090
            },
            {
                "videoid": 3920,
                "model_id": 1090
            },
            {
                "videoid": 1159,
                "model_id": 1376
            },
            {
                "videoid": 1441,
                "model_id": 1376
            },
            {
                "videoid": 1525,
                "model_id": 1376
            },
            {
                "videoid": 1629,
                "model_id": 1376
            },
            {
                "videoid": 1816,
                "model_id": 1376
            },
            {
                "videoid": 1943,
                "model_id": 1376
            },
            {
                "videoid": 1989,
                "model_id": 1376
            },
            {
                "videoid": 2094,
                "model_id": 1376
            },
            {
                "videoid": 2193,
                "model_id": 1376
            },
            {
                "videoid": 2324,
                "model_id": 1376
            },
            {
                "videoid": 2490,
                "model_id": 1376
            },
            {
                "videoid": 2491,
                "model_id": 1376
            },
            {
                "videoid": 2492,
                "model_id": 1376
            },
            {
                "videoid": 2599,
                "model_id": 1376
            },
            {
                "videoid": 3024,
                "model_id": 1376
            },
            {
                "videoid": 4356,
                "model_id": 1376
            },
            {
                "videoid": 4358,
                "model_id": 1376
            },
            {
                "videoid": 4359,
                "model_id": 1376
            },
            {
                "videoid": 4362,
                "model_id": 1376
            },
            {
                "videoid": 4363,
                "model_id": 1376
            },
            {
                "videoid": 4364,
                "model_id": 1376
            },
            {
                "videoid": 4365,
                "model_id": 1376
            },
            {
                "videoid": 4367,
                "model_id": 1376
            },
            {
                "videoid": 4368,
                "model_id": 1376
            },
            {
                "videoid": 4370,
                "model_id": 1376
            },
            {
                "videoid": 4371,
                "model_id": 1376
            },
            {
                "videoid": 4374,
                "model_id": 1376
            },
            {
                "videoid": 1312,
                "model_id": 1146
            },
            {
                "videoid": 1313,
                "model_id": 1146
            },
            {
                "videoid": 1314,
                "model_id": 1146
            },
            {
                "videoid": 1327,
                "model_id": 1146
            },
            {
                "videoid": 1583,
                "model_id": 1146
            },
            {
                "videoid": 1866,
                "model_id": 1146
            },
            {
                "videoid": 1925,
                "model_id": 1146
            },
            {
                "videoid": 2195,
                "model_id": 1146
            },
            {
                "videoid": 2425,
                "model_id": 1146
            },
            {
                "videoid": 2426,
                "model_id": 1146
            },
            {
                "videoid": 2427,
                "model_id": 1146
            },
            {
                "videoid": 2953,
                "model_id": 1146
            },
            {
                "videoid": 2958,
                "model_id": 1146
            },
            {
                "videoid": 2959,
                "model_id": 1146
            },
            {
                "videoid": 3232,
                "model_id": 1146
            },
            {
                "videoid": 3751,
                "model_id": 1146
            },
            {
                "videoid": 3752,
                "model_id": 1146
            },
            {
                "videoid": 3795,
                "model_id": 1146
            },
            {
                "videoid": 3802,
                "model_id": 1146
            },
            {
                "videoid": 3815,
                "model_id": 1146
            },
            {
                "videoid": 3822,
                "model_id": 1146
            },
            {
                "videoid": 3824,
                "model_id": 1146
            },
            {
                "videoid": 3836,
                "model_id": 1146
            },
            {
                "videoid": 3844,
                "model_id": 1146
            },
            {
                "videoid": 1137,
                "model_id": 1381
            },
            {
                "videoid": 1305,
                "model_id": 1381
            },
            {
                "videoid": 1694,
                "model_id": 1381
            },
            {
                "videoid": 1695,
                "model_id": 1381
            },
            {
                "videoid": 1987,
                "model_id": 1381
            },
            {
                "videoid": 2141,
                "model_id": 1381
            },
            {
                "videoid": 2248,
                "model_id": 1381
            },
            {
                "videoid": 2249,
                "model_id": 1381
            },
            {
                "videoid": 2419,
                "model_id": 1381
            },
            {
                "videoid": 2534,
                "model_id": 1381
            },
            {
                "videoid": 2535,
                "model_id": 1381
            },
            {
                "videoid": 2689,
                "model_id": 1381
            },
            {
                "videoid": 2796,
                "model_id": 1381
            },
            {
                "videoid": 2797,
                "model_id": 1381
            },
            {
                "videoid": 3227,
                "model_id": 1381
            },
            {
                "videoid": 3771,
                "model_id": 1381
            },
            {
                "videoid": 3809,
                "model_id": 1381
            },
            {
                "videoid": 1275,
                "model_id": 1401
            },
            {
                "videoid": 1376,
                "model_id": 1401
            },
            {
                "videoid": 1615,
                "model_id": 1401
            },
            {
                "videoid": 1750,
                "model_id": 1401
            },
            {
                "videoid": 1910,
                "model_id": 1401
            },
            {
                "videoid": 1911,
                "model_id": 1401
            },
            {
                "videoid": 1912,
                "model_id": 1401
            },
            {
                "videoid": 2003,
                "model_id": 1401
            },
            {
                "videoid": 2177,
                "model_id": 1401
            },
            {
                "videoid": 2178,
                "model_id": 1401
            },
            {
                "videoid": 2180,
                "model_id": 1401
            },
            {
                "videoid": 2472,
                "model_id": 1401
            },
            {
                "videoid": 2473,
                "model_id": 1401
            },
            {
                "videoid": 2853,
                "model_id": 1401
            },
            {
                "videoid": 2991,
                "model_id": 1401
            },
            {
                "videoid": 3410,
                "model_id": 1401
            },
            {
                "videoid": 3582,
                "model_id": 1401
            },
            {
                "videoid": 4121,
                "model_id": 1401
            },
            {
                "videoid": 4134,
                "model_id": 1401
            },
            {
                "videoid": 4176,
                "model_id": 1401
            },
            {
                "videoid": 4189,
                "model_id": 1401
            },
            {
                "videoid": 4201,
                "model_id": 1401
            },
            {
                "videoid": 4224,
                "model_id": 1401
            },
            {
                "videoid": 4248,
                "model_id": 1401
            },
            {
                "videoid": 1251,
                "model_id": 1296
            },
            {
                "videoid": 1362,
                "model_id": 1296
            },
            {
                "videoid": 1418,
                "model_id": 1296
            },
            {
                "videoid": 1834,
                "model_id": 1296
            },
            {
                "videoid": 2085,
                "model_id": 1296
            },
            {
                "videoid": 2349,
                "model_id": 1296
            },
            {
                "videoid": 2401,
                "model_id": 1296
            },
            {
                "videoid": 2551,
                "model_id": 1296
            },
            {
                "videoid": 2623,
                "model_id": 1296
            },
            {
                "videoid": 2626,
                "model_id": 1296
            },
            {
                "videoid": 2781,
                "model_id": 1296
            },
            {
                "videoid": 2813,
                "model_id": 1296
            },
            {
                "videoid": 3013,
                "model_id": 1296
            },
            {
                "videoid": 3295,
                "model_id": 1296
            },
            {
                "videoid": 3309,
                "model_id": 1296
            },
            {
                "videoid": 3386,
                "model_id": 1296
            },
            {
                "videoid": 3415,
                "model_id": 1296
            },
            {
                "videoid": 3420,
                "model_id": 1296
            },
            {
                "videoid": 3505,
                "model_id": 1296
            },
            {
                "videoid": 3529,
                "model_id": 1296
            },
            {
                "videoid": 3595,
                "model_id": 1296
            },
            {
                "videoid": 3627,
                "model_id": 1296
            },
            {
                "videoid": 3681,
                "model_id": 1296
            },
            {
                "videoid": 3713,
                "model_id": 1296
            },
            {
                "videoid": 1346,
                "model_id": 1380
            },
            {
                "videoid": 1466,
                "model_id": 1380
            },
            {
                "videoid": 1551,
                "model_id": 1380
            },
            {
                "videoid": 1724,
                "model_id": 1380
            },
            {
                "videoid": 1747,
                "model_id": 1380
            },
            {
                "videoid": 1796,
                "model_id": 1380
            },
            {
                "videoid": 2024,
                "model_id": 1380
            },
            {
                "videoid": 2397,
                "model_id": 1380
            },
            {
                "videoid": 2738,
                "model_id": 1380
            },
            {
                "videoid": 2908,
                "model_id": 1380
            },
            {
                "videoid": 3077,
                "model_id": 1380
            },
            {
                "videoid": 3100,
                "model_id": 1380
            },
            {
                "videoid": 3155,
                "model_id": 1380
            },
            {
                "videoid": 3161,
                "model_id": 1380
            },
            {
                "videoid": 3265,
                "model_id": 1380
            },
            {
                "videoid": 3547,
                "model_id": 1380
            },
            {
                "videoid": 4073,
                "model_id": 1380
            },
            {
                "videoid": 4077,
                "model_id": 1380
            },
            {
                "videoid": 4113,
                "model_id": 1380
            },
            {
                "videoid": 4129,
                "model_id": 1380
            },
            {
                "videoid": 4168,
                "model_id": 1380
            },
            {
                "videoid": 4169,
                "model_id": 1380
            },
            {
                "videoid": 4216,
                "model_id": 1380
            },
            {
                "videoid": 4253,
                "model_id": 1380
            },
            {
                "videoid": 1222,
                "model_id": 1137
            },
            {
                "videoid": 1233,
                "model_id": 1137
            },
            {
                "videoid": 1244,
                "model_id": 1137
            },
            {
                "videoid": 1270,
                "model_id": 1137
            },
            {
                "videoid": 1420,
                "model_id": 1137
            },
            {
                "videoid": 1431,
                "model_id": 1137
            },
            {
                "videoid": 1546,
                "model_id": 1137
            },
            {
                "videoid": 1765,
                "model_id": 1137
            },
            {
                "videoid": 1843,
                "model_id": 1137
            },
            {
                "videoid": 1901,
                "model_id": 1137
            },
            {
                "videoid": 2168,
                "model_id": 1137
            },
            {
                "videoid": 2463,
                "model_id": 1137
            },
            {
                "videoid": 2467,
                "model_id": 1137
            },
            {
                "videoid": 2809,
                "model_id": 1137
            },
            {
                "videoid": 3259,
                "model_id": 1137
            },
            {
                "videoid": 3376,
                "model_id": 1137
            },
            {
                "videoid": 3416,
                "model_id": 1137
            },
            {
                "videoid": 3440,
                "model_id": 1137
            },
            {
                "videoid": 3462,
                "model_id": 1137
            },
            {
                "videoid": 3490,
                "model_id": 1137
            },
            {
                "videoid": 3496,
                "model_id": 1137
            },
            {
                "videoid": 3551,
                "model_id": 1137
            },
            {
                "videoid": 3590,
                "model_id": 1137
            },
            {
                "videoid": 3607,
                "model_id": 1137
            },
            {
                "videoid": 3628,
                "model_id": 1137
            },
            {
                "videoid": 3647,
                "model_id": 1137
            },
            {
                "videoid": 3676,
                "model_id": 1137
            },
            {
                "videoid": 3728,
                "model_id": 1137
            },
            {
                "videoid": 4269,
                "model_id": 1137
            },
            {
                "videoid": 4270,
                "model_id": 1137
            },
            {
                "videoid": 4274,
                "model_id": 1137
            },
            {
                "videoid": 4280,
                "model_id": 1137
            },
            {
                "videoid": 4305,
                "model_id": 1137
            },
            {
                "videoid": 4306,
                "model_id": 1137
            },
            {
                "videoid": 4313,
                "model_id": 1137
            },
            {
                "videoid": 4321,
                "model_id": 1137
            },
            {
                "videoid": 4329,
                "model_id": 1137
            },
            {
                "videoid": 4331,
                "model_id": 1137
            },
            {
                "videoid": 4338,
                "model_id": 1137
            },
            {
                "videoid": 4341,
                "model_id": 1137
            },
            {
                "videoid": 1169,
                "model_id": 1379
            },
            {
                "videoid": 1200,
                "model_id": 1379
            },
            {
                "videoid": 1204,
                "model_id": 1379
            },
            {
                "videoid": 1764,
                "model_id": 1379
            },
            {
                "videoid": 1806,
                "model_id": 1379
            },
            {
                "videoid": 1808,
                "model_id": 1379
            },
            {
                "videoid": 2354,
                "model_id": 1379
            },
            {
                "videoid": 2556,
                "model_id": 1379
            },
            {
                "videoid": 2642,
                "model_id": 1379
            },
            {
                "videoid": 2732,
                "model_id": 1379
            },
            {
                "videoid": 2737,
                "model_id": 1379
            },
            {
                "videoid": 2877,
                "model_id": 1379
            },
            {
                "videoid": 2924,
                "model_id": 1379
            },
            {
                "videoid": 3106,
                "model_id": 1379
            },
            {
                "videoid": 3365,
                "model_id": 1379
            },
            {
                "videoid": 3398,
                "model_id": 1379
            },
            {
                "videoid": 3421,
                "model_id": 1379
            },
            {
                "videoid": 3465,
                "model_id": 1379
            },
            {
                "videoid": 3474,
                "model_id": 1379
            },
            {
                "videoid": 3500,
                "model_id": 1379
            },
            {
                "videoid": 3530,
                "model_id": 1379
            },
            {
                "videoid": 3566,
                "model_id": 1379
            },
            {
                "videoid": 3602,
                "model_id": 1379
            },
            {
                "videoid": 3658,
                "model_id": 1379
            },
            {
                "videoid": 3670,
                "model_id": 1379
            },
            {
                "videoid": 3688,
                "model_id": 1379
            },
            {
                "videoid": 4089,
                "model_id": 1379
            },
            {
                "videoid": 4091,
                "model_id": 1379
            },
            {
                "videoid": 4103,
                "model_id": 1379
            },
            {
                "videoid": 4128,
                "model_id": 1379
            },
            {
                "videoid": 4170,
                "model_id": 1379
            },
            {
                "videoid": 4181,
                "model_id": 1379
            },
            {
                "videoid": 4185,
                "model_id": 1379
            },
            {
                "videoid": 4241,
                "model_id": 1379
            },
            {
                "videoid": 4254,
                "model_id": 1379
            },
            {
                "videoid": 4256,
                "model_id": 1379
            },
            {
                "videoid": 1248,
                "model_id": 1131
            },
            {
                "videoid": 1271,
                "model_id": 1131
            },
            {
                "videoid": 1467,
                "model_id": 1131
            },
            {
                "videoid": 1624,
                "model_id": 1131
            },
            {
                "videoid": 1916,
                "model_id": 1131
            },
            {
                "videoid": 2033,
                "model_id": 1131
            },
            {
                "videoid": 2034,
                "model_id": 1131
            },
            {
                "videoid": 2158,
                "model_id": 1131
            },
            {
                "videoid": 2480,
                "model_id": 1131
            },
            {
                "videoid": 2821,
                "model_id": 1131
            },
            {
                "videoid": 2883,
                "model_id": 1131
            },
            {
                "videoid": 2998,
                "model_id": 1131
            },
            {
                "videoid": 3023,
                "model_id": 1131
            },
            {
                "videoid": 3209,
                "model_id": 1131
            },
            {
                "videoid": 3212,
                "model_id": 1131
            },
            {
                "videoid": 3402,
                "model_id": 1131
            },
            {
                "videoid": 3479,
                "model_id": 1131
            },
            {
                "videoid": 3577,
                "model_id": 1131
            },
            {
                "videoid": 3701,
                "model_id": 1131
            },
            {
                "videoid": 1163,
                "model_id": 1377
            },
            {
                "videoid": 1272,
                "model_id": 1377
            },
            {
                "videoid": 1468,
                "model_id": 1377
            },
            {
                "videoid": 1513,
                "model_id": 1377
            },
            {
                "videoid": 2019,
                "model_id": 1377
            },
            {
                "videoid": 2021,
                "model_id": 1377
            },
            {
                "videoid": 2086,
                "model_id": 1377
            },
            {
                "videoid": 2183,
                "model_id": 1377
            },
            {
                "videoid": 2272,
                "model_id": 1377
            },
            {
                "videoid": 2337,
                "model_id": 1377
            },
            {
                "videoid": 2341,
                "model_id": 1377
            },
            {
                "videoid": 2476,
                "model_id": 1377
            },
            {
                "videoid": 2584,
                "model_id": 1377
            },
            {
                "videoid": 3132,
                "model_id": 1377
            },
            {
                "videoid": 3273,
                "model_id": 1377
            },
            {
                "videoid": 3364,
                "model_id": 1377
            },
            {
                "videoid": 3528,
                "model_id": 1377
            },
            {
                "videoid": 3684,
                "model_id": 1377
            },
            {
                "videoid": 4344,
                "model_id": 1377
            },
            {
                "videoid": 4345,
                "model_id": 1377
            },
            {
                "videoid": 4346,
                "model_id": 1377
            },
            {
                "videoid": 4347,
                "model_id": 1377
            },
            {
                "videoid": 4348,
                "model_id": 1377
            },
            {
                "videoid": 4349,
                "model_id": 1377
            },
            {
                "videoid": 4350,
                "model_id": 1377
            },
            {
                "videoid": 4351,
                "model_id": 1377
            },
            {
                "videoid": 4352,
                "model_id": 1377
            },
            {
                "videoid": 4353,
                "model_id": 1377
            },
            {
                "videoid": 4354,
                "model_id": 1377
            },
            {
                "videoid": 4355,
                "model_id": 1377
            },
            {
                "videoid": 1186,
                "model_id": 1394
            },
            {
                "videoid": 1342,
                "model_id": 1394
            },
            {
                "videoid": 1345,
                "model_id": 1394
            },
            {
                "videoid": 1347,
                "model_id": 1394
            },
            {
                "videoid": 1463,
                "model_id": 1394
            },
            {
                "videoid": 1496,
                "model_id": 1394
            },
            {
                "videoid": 1708,
                "model_id": 1394
            },
            {
                "videoid": 1744,
                "model_id": 1394
            },
            {
                "videoid": 1762,
                "model_id": 1394
            },
            {
                "videoid": 2172,
                "model_id": 1394
            },
            {
                "videoid": 2618,
                "model_id": 1394
            },
            {
                "videoid": 2651,
                "model_id": 1394
            },
            {
                "videoid": 2736,
                "model_id": 1394
            },
            {
                "videoid": 2986,
                "model_id": 1394
            },
            {
                "videoid": 3187,
                "model_id": 1394
            },
            {
                "videoid": 3370,
                "model_id": 1394
            },
            {
                "videoid": 3485,
                "model_id": 1394
            },
            {
                "videoid": 3584,
                "model_id": 1394
            },
            {
                "videoid": 3636,
                "model_id": 1394
            },
            {
                "videoid": 3666,
                "model_id": 1394
            },
            {
                "videoid": 3716,
                "model_id": 1394
            },
            {
                "videoid": 3725,
                "model_id": 1394
            },
            {
                "videoid": 4099,
                "model_id": 1394
            },
            {
                "videoid": 4116,
                "model_id": 1394
            },
            {
                "videoid": 4123,
                "model_id": 1394
            },
            {
                "videoid": 4167,
                "model_id": 1394
            },
            {
                "videoid": 4187,
                "model_id": 1394
            },
            {
                "videoid": 4206,
                "model_id": 1394
            },
            {
                "videoid": 4223,
                "model_id": 1394
            },
            {
                "videoid": 4232,
                "model_id": 1394
            },
            {
                "videoid": 4263,
                "model_id": 1394
            },
            {
                "videoid": 1174,
                "model_id": 1119
            },
            {
                "videoid": 1422,
                "model_id": 1119
            },
            {
                "videoid": 1500,
                "model_id": 1119
            },
            {
                "videoid": 1690,
                "model_id": 1119
            },
            {
                "videoid": 1838,
                "model_id": 1119
            },
            {
                "videoid": 2098,
                "model_id": 1119
            },
            {
                "videoid": 2300,
                "model_id": 1119
            },
            {
                "videoid": 2344,
                "model_id": 1119
            },
            {
                "videoid": 2351,
                "model_id": 1119
            },
            {
                "videoid": 2654,
                "model_id": 1119
            },
            {
                "videoid": 2795,
                "model_id": 1119
            },
            {
                "videoid": 2898,
                "model_id": 1119
            },
            {
                "videoid": 2928,
                "model_id": 1119
            },
            {
                "videoid": 3069,
                "model_id": 1119
            },
            {
                "videoid": 3197,
                "model_id": 1119
            },
            {
                "videoid": 3360,
                "model_id": 1119
            },
            {
                "videoid": 3362,
                "model_id": 1119
            },
            {
                "videoid": 3405,
                "model_id": 1119
            },
            {
                "videoid": 3427,
                "model_id": 1119
            },
            {
                "videoid": 3445,
                "model_id": 1119
            },
            {
                "videoid": 3501,
                "model_id": 1119
            },
            {
                "videoid": 3517,
                "model_id": 1119
            },
            {
                "videoid": 3526,
                "model_id": 1119
            },
            {
                "videoid": 3576,
                "model_id": 1119
            },
            {
                "videoid": 3593,
                "model_id": 1119
            },
            {
                "videoid": 3613,
                "model_id": 1119
            },
            {
                "videoid": 3617,
                "model_id": 1119
            },
            {
                "videoid": 3632,
                "model_id": 1119
            },
            {
                "videoid": 3686,
                "model_id": 1119
            },
            {
                "videoid": 3704,
                "model_id": 1119
            },
            {
                "videoid": 3712,
                "model_id": 1119
            },
            {
                "videoid": 4267,
                "model_id": 1119
            },
            {
                "videoid": 4278,
                "model_id": 1119
            },
            {
                "videoid": 4282,
                "model_id": 1119
            },
            {
                "videoid": 4307,
                "model_id": 1119
            },
            {
                "videoid": 4311,
                "model_id": 1119
            },
            {
                "videoid": 4312,
                "model_id": 1119
            },
            {
                "videoid": 4319,
                "model_id": 1119
            },
            {
                "videoid": 4322,
                "model_id": 1119
            },
            {
                "videoid": 4343,
                "model_id": 1119
            },
            {
                "videoid": 1149,
                "model_id": 1138
            },
            {
                "videoid": 1214,
                "model_id": 1138
            },
            {
                "videoid": 1348,
                "model_id": 1138
            },
            {
                "videoid": 1700,
                "model_id": 1138
            },
            {
                "videoid": 1767,
                "model_id": 1138
            },
            {
                "videoid": 1997,
                "model_id": 1138
            },
            {
                "videoid": 2264,
                "model_id": 1138
            },
            {
                "videoid": 2304,
                "model_id": 1138
            },
            {
                "videoid": 2629,
                "model_id": 1138
            },
            {
                "videoid": 2869,
                "model_id": 1138
            },
            {
                "videoid": 2871,
                "model_id": 1138
            },
            {
                "videoid": 3089,
                "model_id": 1138
            },
            {
                "videoid": 3121,
                "model_id": 1138
            },
            {
                "videoid": 3272,
                "model_id": 1138
            },
            {
                "videoid": 3431,
                "model_id": 1138
            },
            {
                "videoid": 3599,
                "model_id": 1138
            },
            {
                "videoid": 4283,
                "model_id": 1138
            },
            {
                "videoid": 4292,
                "model_id": 1138
            },
            {
                "videoid": 4294,
                "model_id": 1138
            },
            {
                "videoid": 4295,
                "model_id": 1138
            },
            {
                "videoid": 4300,
                "model_id": 1138
            },
            {
                "videoid": 4301,
                "model_id": 1138
            },
            {
                "videoid": 4328,
                "model_id": 1138
            },
            {
                "videoid": 4332,
                "model_id": 1138
            },
            {
                "videoid": 4335,
                "model_id": 1138
            },
            {
                "videoid": 4340,
                "model_id": 1138
            },
            {
                "videoid": 4342,
                "model_id": 1138
            },
            {
                "videoid": 1221,
                "model_id": 1133
            },
            {
                "videoid": 1278,
                "model_id": 1133
            },
            {
                "videoid": 1519,
                "model_id": 1133
            },
            {
                "videoid": 1617,
                "model_id": 1133
            },
            {
                "videoid": 1618,
                "model_id": 1133
            },
            {
                "videoid": 1733,
                "model_id": 1133
            },
            {
                "videoid": 1984,
                "model_id": 1133
            },
            {
                "videoid": 2064,
                "model_id": 1133
            },
            {
                "videoid": 2294,
                "model_id": 1133
            },
            {
                "videoid": 2331,
                "model_id": 1133
            },
            {
                "videoid": 2573,
                "model_id": 1133
            },
            {
                "videoid": 2837,
                "model_id": 1133
            },
            {
                "videoid": 2987,
                "model_id": 1133
            },
            {
                "videoid": 2988,
                "model_id": 1133
            },
            {
                "videoid": 3274,
                "model_id": 1133
            },
            {
                "videoid": 3369,
                "model_id": 1133
            },
            {
                "videoid": 3378,
                "model_id": 1133
            },
            {
                "videoid": 3412,
                "model_id": 1133
            },
            {
                "videoid": 3491,
                "model_id": 1133
            },
            {
                "videoid": 3539,
                "model_id": 1133
            },
            {
                "videoid": 3580,
                "model_id": 1133
            },
            {
                "videoid": 3645,
                "model_id": 1133
            },
            {
                "videoid": 3675,
                "model_id": 1133
            },
            {
                "videoid": 3720,
                "model_id": 1133
            },
            {
                "videoid": 4377,
                "model_id": 1133
            },
            {
                "videoid": 4385,
                "model_id": 1133
            },
            {
                "videoid": 4404,
                "model_id": 1133
            },
            {
                "videoid": 4405,
                "model_id": 1133
            },
            {
                "videoid": 4408,
                "model_id": 1133
            },
            {
                "videoid": 4421,
                "model_id": 1133
            },
            {
                "videoid": 4422,
                "model_id": 1133
            },
            {
                "videoid": 4424,
                "model_id": 1133
            },
            {
                "videoid": 4425,
                "model_id": 1133
            },
            {
                "videoid": 4438,
                "model_id": 1133
            },
            {
                "videoid": 4440,
                "model_id": 1133
            },
            {
                "videoid": 4442,
                "model_id": 1133
            },
            {
                "videoid": 1357,
                "model_id": 1238
            },
            {
                "videoid": 1414,
                "model_id": 1238
            },
            {
                "videoid": 1415,
                "model_id": 1238
            },
            {
                "videoid": 1529,
                "model_id": 1238
            },
            {
                "videoid": 1544,
                "model_id": 1238
            },
            {
                "videoid": 1553,
                "model_id": 1238
            },
            {
                "videoid": 1918,
                "model_id": 1238
            },
            {
                "videoid": 1919,
                "model_id": 1238
            },
            {
                "videoid": 2373,
                "model_id": 1238
            },
            {
                "videoid": 2558,
                "model_id": 1238
            },
            {
                "videoid": 2600,
                "model_id": 1238
            },
            {
                "videoid": 2607,
                "model_id": 1238
            },
            {
                "videoid": 2613,
                "model_id": 1238
            },
            {
                "videoid": 2791,
                "model_id": 1238
            },
            {
                "videoid": 2822,
                "model_id": 1238
            },
            {
                "videoid": 2995,
                "model_id": 1238
            },
            {
                "videoid": 3003,
                "model_id": 1238
            },
            {
                "videoid": 3150,
                "model_id": 1238
            },
            {
                "videoid": 3358,
                "model_id": 1238
            },
            {
                "videoid": 3451,
                "model_id": 1238
            },
            {
                "videoid": 4272,
                "model_id": 1238
            },
            {
                "videoid": 4275,
                "model_id": 1238
            },
            {
                "videoid": 4302,
                "model_id": 1238
            },
            {
                "videoid": 4303,
                "model_id": 1238
            },
            {
                "videoid": 4314,
                "model_id": 1238
            },
            {
                "videoid": 4315,
                "model_id": 1238
            },
            {
                "videoid": 4317,
                "model_id": 1238
            },
            {
                "videoid": 4318,
                "model_id": 1238
            },
            {
                "videoid": 4323,
                "model_id": 1238
            },
            {
                "videoid": 4330,
                "model_id": 1238
            },
            {
                "videoid": 1176,
                "model_id": 1152
            },
            {
                "videoid": 1352,
                "model_id": 1152
            },
            {
                "videoid": 1432,
                "model_id": 1152
            },
            {
                "videoid": 1528,
                "model_id": 1152
            },
            {
                "videoid": 1809,
                "model_id": 1152
            },
            {
                "videoid": 1817,
                "model_id": 1152
            },
            {
                "videoid": 1915,
                "model_id": 1152
            },
            {
                "videoid": 1917,
                "model_id": 1152
            },
            {
                "videoid": 1942,
                "model_id": 1152
            },
            {
                "videoid": 2100,
                "model_id": 1152
            },
            {
                "videoid": 2310,
                "model_id": 1152
            },
            {
                "videoid": 2485,
                "model_id": 1152
            },
            {
                "videoid": 2874,
                "model_id": 1152
            },
            {
                "videoid": 2994,
                "model_id": 1152
            },
            {
                "videoid": 3204,
                "model_id": 1152
            },
            {
                "videoid": 3384,
                "model_id": 1152
            },
            {
                "videoid": 3552,
                "model_id": 1152
            },
            {
                "videoid": 3625,
                "model_id": 1152
            },
            {
                "videoid": 3679,
                "model_id": 1152
            },
            {
                "videoid": 3731,
                "model_id": 1152
            },
            {
                "videoid": 1253,
                "model_id": 1196
            },
            {
                "videoid": 1350,
                "model_id": 1196
            },
            {
                "videoid": 1423,
                "model_id": 1196
            },
            {
                "videoid": 1504,
                "model_id": 1196
            },
            {
                "videoid": 1549,
                "model_id": 1196
            },
            {
                "videoid": 1779,
                "model_id": 1196
            },
            {
                "videoid": 1829,
                "model_id": 1196
            },
            {
                "videoid": 1939,
                "model_id": 1196
            },
            {
                "videoid": 1995,
                "model_id": 1196
            },
            {
                "videoid": 2046,
                "model_id": 1196
            },
            {
                "videoid": 2121,
                "model_id": 1196
            },
            {
                "videoid": 2320,
                "model_id": 1196
            },
            {
                "videoid": 2376,
                "model_id": 1196
            },
            {
                "videoid": 2656,
                "model_id": 1196
            },
            {
                "videoid": 3179,
                "model_id": 1196
            },
            {
                "videoid": 3535,
                "model_id": 1196
            },
            {
                "videoid": 2139,
                "model_id": 1301
            },
            {
                "videoid": 2142,
                "model_id": 1301
            },
            {
                "videoid": 2421,
                "model_id": 1301
            },
            {
                "videoid": 2422,
                "model_id": 1301
            },
            {
                "videoid": 2442,
                "model_id": 1301
            },
            {
                "videoid": 2719,
                "model_id": 1301
            },
            {
                "videoid": 2947,
                "model_id": 1301
            },
            {
                "videoid": 2948,
                "model_id": 1301
            },
            {
                "videoid": 2972,
                "model_id": 1301
            },
            {
                "videoid": 2976,
                "model_id": 1301
            },
            {
                "videoid": 3229,
                "model_id": 1301
            },
            {
                "videoid": 3770,
                "model_id": 1301
            },
            {
                "videoid": 3772,
                "model_id": 1301
            },
            {
                "videoid": 3807,
                "model_id": 1301
            },
            {
                "videoid": 3812,
                "model_id": 1301
            },
            {
                "videoid": 3834,
                "model_id": 1301
            },
            {
                "videoid": 3845,
                "model_id": 1301
            },
            {
                "videoid": 1308,
                "model_id": 1093
            },
            {
                "videoid": 1579,
                "model_id": 1093
            },
            {
                "videoid": 1860,
                "model_id": 1093
            },
            {
                "videoid": 1861,
                "model_id": 1093
            },
            {
                "videoid": 1868,
                "model_id": 1093
            },
            {
                "videoid": 1877,
                "model_id": 1093
            },
            {
                "videoid": 2145,
                "model_id": 1093
            },
            {
                "videoid": 2154,
                "model_id": 1093
            },
            {
                "videoid": 2155,
                "model_id": 1093
            },
            {
                "videoid": 2424,
                "model_id": 1093
            },
            {
                "videoid": 2692,
                "model_id": 1093
            },
            {
                "videoid": 2693,
                "model_id": 1093
            },
            {
                "videoid": 3230,
                "model_id": 1093
            },
            {
                "videoid": 3233,
                "model_id": 1093
            },
            {
                "videoid": 3762,
                "model_id": 1093
            },
            {
                "videoid": 3765,
                "model_id": 1093
            },
            {
                "videoid": 3777,
                "model_id": 1093
            },
            {
                "videoid": 3778,
                "model_id": 1093
            },
            {
                "videoid": 3781,
                "model_id": 1093
            },
            {
                "videoid": 3791,
                "model_id": 1093
            },
            {
                "videoid": 3797,
                "model_id": 1093
            },
            {
                "videoid": 3803,
                "model_id": 1093
            },
            {
                "videoid": 3805,
                "model_id": 1093
            },
            {
                "videoid": 3814,
                "model_id": 1093
            },
            {
                "videoid": 1274,
                "model_id": 1150
            },
            {
                "videoid": 1611,
                "model_id": 1150
            },
            {
                "videoid": 1788,
                "model_id": 1150
            },
            {
                "videoid": 1981,
                "model_id": 1150
            },
            {
                "videoid": 2001,
                "model_id": 1150
            },
            {
                "videoid": 2047,
                "model_id": 1150
            },
            {
                "videoid": 2053,
                "model_id": 1150
            },
            {
                "videoid": 2174,
                "model_id": 1150
            },
            {
                "videoid": 2280,
                "model_id": 1150
            },
            {
                "videoid": 2645,
                "model_id": 1150
            },
            {
                "videoid": 2926,
                "model_id": 1150
            },
            {
                "videoid": 3171,
                "model_id": 1150
            },
            {
                "videoid": 3199,
                "model_id": 1150
            },
            {
                "videoid": 3264,
                "model_id": 1150
            },
            {
                "videoid": 3267,
                "model_id": 1150
            },
            {
                "videoid": 3392,
                "model_id": 1150
            },
            {
                "videoid": 3417,
                "model_id": 1150
            },
            {
                "videoid": 3463,
                "model_id": 1150
            },
            {
                "videoid": 3522,
                "model_id": 1150
            },
            {
                "videoid": 3555,
                "model_id": 1150
            },
            {
                "videoid": 3589,
                "model_id": 1150
            },
            {
                "videoid": 3651,
                "model_id": 1150
            },
            {
                "videoid": 3706,
                "model_id": 1150
            },
            {
                "videoid": 3957,
                "model_id": 1150
            },
            {
                "videoid": 3969,
                "model_id": 1150
            },
            {
                "videoid": 3985,
                "model_id": 1150
            },
            {
                "videoid": 3986,
                "model_id": 1150
            },
            {
                "videoid": 3988,
                "model_id": 1150
            },
            {
                "videoid": 3990,
                "model_id": 1150
            },
            {
                "videoid": 4002,
                "model_id": 1150
            },
            {
                "videoid": 4004,
                "model_id": 1150
            },
            {
                "videoid": 4007,
                "model_id": 1150
            },
            {
                "videoid": 4014,
                "model_id": 1150
            },
            {
                "videoid": 4015,
                "model_id": 1150
            },
            {
                "videoid": 4016,
                "model_id": 1150
            },
            {
                "videoid": 4018,
                "model_id": 1150
            },
            {
                "videoid": 4022,
                "model_id": 1150
            },
            {
                "videoid": 1250,
                "model_id": 1395
            },
            {
                "videoid": 1259,
                "model_id": 1395
            },
            {
                "videoid": 1280,
                "model_id": 1395
            },
            {
                "videoid": 1811,
                "model_id": 1395
            },
            {
                "videoid": 1897,
                "model_id": 1395
            },
            {
                "videoid": 1900,
                "model_id": 1395
            },
            {
                "videoid": 2106,
                "model_id": 1395
            },
            {
                "videoid": 2107,
                "model_id": 1395
            },
            {
                "videoid": 2169,
                "model_id": 1395
            },
            {
                "videoid": 2398,
                "model_id": 1395
            },
            {
                "videoid": 2505,
                "model_id": 1395
            },
            {
                "videoid": 2553,
                "model_id": 1395
            },
            {
                "videoid": 2907,
                "model_id": 1395
            },
            {
                "videoid": 2920,
                "model_id": 1395
            },
            {
                "videoid": 3195,
                "model_id": 1395
            },
            {
                "videoid": 3424,
                "model_id": 1395
            },
            {
                "videoid": 3596,
                "model_id": 1395
            },
            {
                "videoid": 3857,
                "model_id": 1395
            },
            {
                "videoid": 3868,
                "model_id": 1395
            },
            {
                "videoid": 3879,
                "model_id": 1395
            },
            {
                "videoid": 3891,
                "model_id": 1395
            },
            {
                "videoid": 3893,
                "model_id": 1395
            },
            {
                "videoid": 3903,
                "model_id": 1395
            },
            {
                "videoid": 3907,
                "model_id": 1395
            },
            {
                "videoid": 3918,
                "model_id": 1395
            },
            {
                "videoid": 3919,
                "model_id": 1395
            },
            {
                "videoid": 3932,
                "model_id": 1395
            },
            {
                "videoid": 3933,
                "model_id": 1395
            },
            {
                "videoid": 1543,
                "model_id": 1353
            },
            {
                "videoid": 1607,
                "model_id": 1353
            },
            {
                "videoid": 1899,
                "model_id": 1353
            },
            {
                "videoid": 2308,
                "model_id": 1353
            },
            {
                "videoid": 2384,
                "model_id": 1353
            },
            {
                "videoid": 2466,
                "model_id": 1353
            },
            {
                "videoid": 2469,
                "model_id": 1353
            },
            {
                "videoid": 2559,
                "model_id": 1353
            },
            {
                "videoid": 2575,
                "model_id": 1353
            },
            {
                "videoid": 2628,
                "model_id": 1353
            },
            {
                "videoid": 2733,
                "model_id": 1353
            },
            {
                "videoid": 2798,
                "model_id": 1353
            },
            {
                "videoid": 3118,
                "model_id": 1353
            },
            {
                "videoid": 3406,
                "model_id": 1353
            },
            {
                "videoid": 3411,
                "model_id": 1353
            },
            {
                "videoid": 3481,
                "model_id": 1353
            },
            {
                "videoid": 3488,
                "model_id": 1353
            },
            {
                "videoid": 3515,
                "model_id": 1353
            },
            {
                "videoid": 3579,
                "model_id": 1353
            },
            {
                "videoid": 3586,
                "model_id": 1353
            },
            {
                "videoid": 3646,
                "model_id": 1353
            },
            {
                "videoid": 3674,
                "model_id": 1353
            },
            {
                "videoid": 3700,
                "model_id": 1353
            },
            {
                "videoid": 4085,
                "model_id": 1353
            },
            {
                "videoid": 4098,
                "model_id": 1353
            },
            {
                "videoid": 4117,
                "model_id": 1353
            },
            {
                "videoid": 4140,
                "model_id": 1353
            },
            {
                "videoid": 4164,
                "model_id": 1353
            },
            {
                "videoid": 4183,
                "model_id": 1353
            },
            {
                "videoid": 4184,
                "model_id": 1353
            },
            {
                "videoid": 4250,
                "model_id": 1353
            },
            {
                "videoid": 4260,
                "model_id": 1353
            },
            {
                "videoid": 4261,
                "model_id": 1353
            },
            {
                "videoid": 1170,
                "model_id": 1192
            },
            {
                "videoid": 1613,
                "model_id": 1192
            },
            {
                "videoid": 1757,
                "model_id": 1192
            },
            {
                "videoid": 1826,
                "model_id": 1192
            },
            {
                "videoid": 2093,
                "model_id": 1192
            },
            {
                "videoid": 2096,
                "model_id": 1192
            },
            {
                "videoid": 2097,
                "model_id": 1192
            },
            {
                "videoid": 2111,
                "model_id": 1192
            },
            {
                "videoid": 2179,
                "model_id": 1192
            },
            {
                "videoid": 2184,
                "model_id": 1192
            },
            {
                "videoid": 2478,
                "model_id": 1192
            },
            {
                "videoid": 2563,
                "model_id": 1192
            },
            {
                "videoid": 2740,
                "model_id": 1192
            },
            {
                "videoid": 3165,
                "model_id": 1192
            },
            {
                "videoid": 3207,
                "model_id": 1192
            },
            {
                "videoid": 3373,
                "model_id": 1192
            },
            {
                "videoid": 3393,
                "model_id": 1192
            },
            {
                "videoid": 3453,
                "model_id": 1192
            },
            {
                "videoid": 3470,
                "model_id": 1192
            },
            {
                "videoid": 3523,
                "model_id": 1192
            },
            {
                "videoid": 3533,
                "model_id": 1192
            },
            {
                "videoid": 3543,
                "model_id": 1192
            },
            {
                "videoid": 3562,
                "model_id": 1192
            },
            {
                "videoid": 3620,
                "model_id": 1192
            },
            {
                "videoid": 3638,
                "model_id": 1192
            },
            {
                "videoid": 3653,
                "model_id": 1192
            },
            {
                "videoid": 3692,
                "model_id": 1192
            },
            {
                "videoid": 3723,
                "model_id": 1192
            },
            {
                "videoid": 1138,
                "model_id": 1342
            },
            {
                "videoid": 1318,
                "model_id": 1342
            },
            {
                "videoid": 1488,
                "model_id": 1342
            },
            {
                "videoid": 1584,
                "model_id": 1342
            },
            {
                "videoid": 1753,
                "model_id": 1342
            },
            {
                "videoid": 1799,
                "model_id": 1342
            },
            {
                "videoid": 2029,
                "model_id": 1342
            },
            {
                "videoid": 2435,
                "model_id": 1342
            },
            {
                "videoid": 2802,
                "model_id": 1342
            },
            {
                "videoid": 2964,
                "model_id": 1342
            },
            {
                "videoid": 2966,
                "model_id": 1342
            },
            {
                "videoid": 3088,
                "model_id": 1342
            },
            {
                "videoid": 3238,
                "model_id": 1342
            },
            {
                "videoid": 3361,
                "model_id": 1342
            },
            {
                "videoid": 3531,
                "model_id": 1342
            },
            {
                "videoid": 3714,
                "model_id": 1342
            },
            {
                "videoid": 3773,
                "model_id": 1342
            },
            {
                "videoid": 3775,
                "model_id": 1342
            },
            {
                "videoid": 3785,
                "model_id": 1342
            },
            {
                "videoid": 3787,
                "model_id": 1342
            },
            {
                "videoid": 3798,
                "model_id": 1342
            },
            {
                "videoid": 3829,
                "model_id": 1342
            },
            {
                "videoid": 3843,
                "model_id": 1342
            },
            {
                "videoid": 1324,
                "model_id": 1400
            },
            {
                "videoid": 1325,
                "model_id": 1400
            },
            {
                "videoid": 1437,
                "model_id": 1400
            },
            {
                "videoid": 1586,
                "model_id": 1400
            },
            {
                "videoid": 1587,
                "model_id": 1400
            },
            {
                "videoid": 1588,
                "model_id": 1400
            },
            {
                "videoid": 1875,
                "model_id": 1400
            },
            {
                "videoid": 1876,
                "model_id": 1400
            },
            {
                "videoid": 2146,
                "model_id": 1400
            },
            {
                "videoid": 2253,
                "model_id": 1400
            },
            {
                "videoid": 2286,
                "model_id": 1400
            },
            {
                "videoid": 2439,
                "model_id": 1400
            },
            {
                "videoid": 2574,
                "model_id": 1400
            },
            {
                "videoid": 3242,
                "model_id": 1400
            },
            {
                "videoid": 3243,
                "model_id": 1400
            },
            {
                "videoid": 3767,
                "model_id": 1400
            },
            {
                "videoid": 3779,
                "model_id": 1400
            },
            {
                "videoid": 3840,
                "model_id": 1400
            },
            {
                "videoid": 1328,
                "model_id": 1341
            },
            {
                "videoid": 1329,
                "model_id": 1341
            },
            {
                "videoid": 1330,
                "model_id": 1341
            },
            {
                "videoid": 1595,
                "model_id": 1341
            },
            {
                "videoid": 1885,
                "model_id": 1341
            },
            {
                "videoid": 2720,
                "model_id": 1341
            },
            {
                "videoid": 2721,
                "model_id": 1341
            },
            {
                "videoid": 2722,
                "model_id": 1341
            },
            {
                "videoid": 2979,
                "model_id": 1341
            },
            {
                "videoid": 3249,
                "model_id": 1341
            },
            {
                "videoid": 3847,
                "model_id": 1341
            },
            {
                "videoid": 3848,
                "model_id": 1341
            },
            {
                "videoid": 3849,
                "model_id": 1341
            },
            {
                "videoid": 3850,
                "model_id": 1341
            },
            {
                "videoid": 3851,
                "model_id": 1341
            },
            {
                "videoid": 3852,
                "model_id": 1341
            },
            {
                "videoid": 3853,
                "model_id": 1341
            },
            {
                "videoid": 3854,
                "model_id": 1341
            },
            {
                "videoid": 3855,
                "model_id": 1341
            },
            {
                "videoid": 3856,
                "model_id": 1341
            },
            {
                "videoid": 1183,
                "model_id": 1101
            },
            {
                "videoid": 1252,
                "model_id": 1101
            },
            {
                "videoid": 1625,
                "model_id": 1101
            },
            {
                "videoid": 1688,
                "model_id": 1101
            },
            {
                "videoid": 1704,
                "model_id": 1101
            },
            {
                "videoid": 1974,
                "model_id": 1101
            },
            {
                "videoid": 1975,
                "model_id": 1101
            },
            {
                "videoid": 1999,
                "model_id": 1101
            },
            {
                "videoid": 2038,
                "model_id": 1101
            },
            {
                "videoid": 2104,
                "model_id": 1101
            },
            {
                "videoid": 2187,
                "model_id": 1101
            },
            {
                "videoid": 2244,
                "model_id": 1101
            },
            {
                "videoid": 2745,
                "model_id": 1101
            },
            {
                "videoid": 2808,
                "model_id": 1101
            },
            {
                "videoid": 2810,
                "model_id": 1101
            },
            {
                "videoid": 2910,
                "model_id": 1101
            },
            {
                "videoid": 3068,
                "model_id": 1101
            },
            {
                "videoid": 3090,
                "model_id": 1101
            },
            {
                "videoid": 3287,
                "model_id": 1101
            },
            {
                "videoid": 3450,
                "model_id": 1101
            },
            {
                "videoid": 3520,
                "model_id": 1101
            },
            {
                "videoid": 3622,
                "model_id": 1101
            },
            {
                "videoid": 4379,
                "model_id": 1101
            },
            {
                "videoid": 4382,
                "model_id": 1101
            },
            {
                "videoid": 4383,
                "model_id": 1101
            },
            {
                "videoid": 4387,
                "model_id": 1101
            },
            {
                "videoid": 4388,
                "model_id": 1101
            },
            {
                "videoid": 4390,
                "model_id": 1101
            },
            {
                "videoid": 4393,
                "model_id": 1101
            },
            {
                "videoid": 4401,
                "model_id": 1101
            },
            {
                "videoid": 4402,
                "model_id": 1101
            },
            {
                "videoid": 4433,
                "model_id": 1101
            },
            {
                "videoid": 4434,
                "model_id": 1101
            },
            {
                "videoid": 1241,
                "model_id": 1234
            },
            {
                "videoid": 1268,
                "model_id": 1234
            },
            {
                "videoid": 1277,
                "model_id": 1234
            },
            {
                "videoid": 1469,
                "model_id": 1234
            },
            {
                "videoid": 1790,
                "model_id": 1234
            },
            {
                "videoid": 1904,
                "model_id": 1234
            },
            {
                "videoid": 2176,
                "model_id": 1234
            },
            {
                "videoid": 2303,
                "model_id": 1234
            },
            {
                "videoid": 2389,
                "model_id": 1234
            },
            {
                "videoid": 2468,
                "model_id": 1234
            },
            {
                "videoid": 2655,
                "model_id": 1234
            },
            {
                "videoid": 2887,
                "model_id": 1234
            },
            {
                "videoid": 3073,
                "model_id": 1234
            },
            {
                "videoid": 3094,
                "model_id": 1234
            },
            {
                "videoid": 3270,
                "model_id": 1234
            },
            {
                "videoid": 1255,
                "model_id": 1149
            },
            {
                "videoid": 1334,
                "model_id": 1149
            },
            {
                "videoid": 1535,
                "model_id": 1149
            },
            {
                "videoid": 1550,
                "model_id": 1149
            },
            {
                "videoid": 1603,
                "model_id": 1149
            },
            {
                "videoid": 1716,
                "model_id": 1149
            },
            {
                "videoid": 1890,
                "model_id": 1149
            },
            {
                "videoid": 2084,
                "model_id": 1149
            },
            {
                "videoid": 2163,
                "model_id": 1149
            },
            {
                "videoid": 2386,
                "model_id": 1149
            },
            {
                "videoid": 2392,
                "model_id": 1149
            },
            {
                "videoid": 2917,
                "model_id": 1149
            },
            {
                "videoid": 2983,
                "model_id": 1149
            },
            {
                "videoid": 3208,
                "model_id": 1149
            },
            {
                "videoid": 3252,
                "model_id": 1149
            },
            {
                "videoid": 3881,
                "model_id": 1149
            },
            {
                "videoid": 3883,
                "model_id": 1149
            },
            {
                "videoid": 3886,
                "model_id": 1149
            },
            {
                "videoid": 3899,
                "model_id": 1149
            },
            {
                "videoid": 3901,
                "model_id": 1149
            },
            {
                "videoid": 3909,
                "model_id": 1149
            },
            {
                "videoid": 3916,
                "model_id": 1149
            },
            {
                "videoid": 3917,
                "model_id": 1149
            },
            {
                "videoid": 3961,
                "model_id": 1149
            },
            {
                "videoid": 4008,
                "model_id": 1149
            },
            {
                "videoid": 4017,
                "model_id": 1149
            },
            {
                "videoid": 1152,
                "model_id": 1384
            },
            {
                "videoid": 1336,
                "model_id": 1384
            },
            {
                "videoid": 1599,
                "model_id": 1384
            },
            {
                "videoid": 1605,
                "model_id": 1384
            },
            {
                "videoid": 1768,
                "model_id": 1384
            },
            {
                "videoid": 2066,
                "model_id": 1384
            },
            {
                "videoid": 2071,
                "model_id": 1384
            },
            {
                "videoid": 2281,
                "model_id": 1384
            },
            {
                "videoid": 2457,
                "model_id": 1384
            },
            {
                "videoid": 2459,
                "model_id": 1384
            },
            {
                "videoid": 2460,
                "model_id": 1384
            },
            {
                "videoid": 2728,
                "model_id": 1384
            },
            {
                "videoid": 2816,
                "model_id": 1384
            },
            {
                "videoid": 3177,
                "model_id": 1384
            },
            {
                "videoid": 3311,
                "model_id": 1384
            },
            {
                "videoid": 3396,
                "model_id": 1384
            },
            {
                "videoid": 3467,
                "model_id": 1384
            },
            {
                "videoid": 3471,
                "model_id": 1384
            },
            {
                "videoid": 3560,
                "model_id": 1384
            },
            {
                "videoid": 3660,
                "model_id": 1384
            },
            {
                "videoid": 3860,
                "model_id": 1384
            },
            {
                "videoid": 3861,
                "model_id": 1384
            },
            {
                "videoid": 3882,
                "model_id": 1384
            },
            {
                "videoid": 3898,
                "model_id": 1384
            },
            {
                "videoid": 3908,
                "model_id": 1384
            },
            {
                "videoid": 3928,
                "model_id": 1384
            },
            {
                "videoid": 3929,
                "model_id": 1384
            },
            {
                "videoid": 3936,
                "model_id": 1384
            },
            {
                "videoid": 1331,
                "model_id": 1387
            },
            {
                "videoid": 1596,
                "model_id": 1387
            },
            {
                "videoid": 1597,
                "model_id": 1387
            },
            {
                "videoid": 1604,
                "model_id": 1387
            },
            {
                "videoid": 1892,
                "model_id": 1387
            },
            {
                "videoid": 2447,
                "model_id": 1387
            },
            {
                "videoid": 2448,
                "model_id": 1387
            },
            {
                "videoid": 2455,
                "model_id": 1387
            },
            {
                "videoid": 2458,
                "model_id": 1387
            },
            {
                "videoid": 2667,
                "model_id": 1387
            },
            {
                "videoid": 2724,
                "model_id": 1387
            },
            {
                "videoid": 2730,
                "model_id": 1387
            },
            {
                "videoid": 3092,
                "model_id": 1387
            },
            {
                "videoid": 3250,
                "model_id": 1387
            },
            {
                "videoid": 3310,
                "model_id": 1387
            },
            {
                "videoid": 3873,
                "model_id": 1387
            },
            {
                "videoid": 3896,
                "model_id": 1387
            },
            {
                "videoid": 3925,
                "model_id": 1387
            },
            {
                "videoid": 1343,
                "model_id": 1140
            },
            {
                "videoid": 1444,
                "model_id": 1140
            },
            {
                "videoid": 1555,
                "model_id": 1140
            },
            {
                "videoid": 1610,
                "model_id": 1140
            },
            {
                "videoid": 1612,
                "model_id": 1140
            },
            {
                "videoid": 1720,
                "model_id": 1140
            },
            {
                "videoid": 1845,
                "model_id": 1140
            },
            {
                "videoid": 2175,
                "model_id": 1140
            },
            {
                "videoid": 2350,
                "model_id": 1140
            },
            {
                "videoid": 2641,
                "model_id": 1140
            },
            {
                "videoid": 2836,
                "model_id": 1140
            },
            {
                "videoid": 2879,
                "model_id": 1140
            },
            {
                "videoid": 3116,
                "model_id": 1140
            },
            {
                "videoid": 3124,
                "model_id": 1140
            },
            {
                "videoid": 3268,
                "model_id": 1140
            },
            {
                "videoid": 3394,
                "model_id": 1140
            },
            {
                "videoid": 3449,
                "model_id": 1140
            },
            {
                "videoid": 3519,
                "model_id": 1140
            },
            {
                "videoid": 3558,
                "model_id": 1140
            },
            {
                "videoid": 3623,
                "model_id": 1140
            },
            {
                "videoid": 3633,
                "model_id": 1140
            },
            {
                "videoid": 3637,
                "model_id": 1140
            },
            {
                "videoid": 3708,
                "model_id": 1140
            },
            {
                "videoid": 3719,
                "model_id": 1140
            },
            {
                "videoid": 4273,
                "model_id": 1140
            },
            {
                "videoid": 4277,
                "model_id": 1140
            },
            {
                "videoid": 4279,
                "model_id": 1140
            },
            {
                "videoid": 4287,
                "model_id": 1140
            },
            {
                "videoid": 4288,
                "model_id": 1140
            },
            {
                "videoid": 4291,
                "model_id": 1140
            },
            {
                "videoid": 4293,
                "model_id": 1140
            },
            {
                "videoid": 4304,
                "model_id": 1140
            },
            {
                "videoid": 4309,
                "model_id": 1140
            },
            {
                "videoid": 4324,
                "model_id": 1140
            },
            {
                "videoid": 4334,
                "model_id": 1140
            },
            {
                "videoid": 4339,
                "model_id": 1140
            },
            {
                "videoid": 1337,
                "model_id": 1141
            },
            {
                "videoid": 1338,
                "model_id": 1141
            },
            {
                "videoid": 1339,
                "model_id": 1141
            },
            {
                "videoid": 1341,
                "model_id": 1141
            },
            {
                "videoid": 1494,
                "model_id": 1141
            },
            {
                "videoid": 2020,
                "model_id": 1141
            },
            {
                "videoid": 2044,
                "model_id": 1141
            },
            {
                "videoid": 2110,
                "model_id": 1141
            },
            {
                "videoid": 2283,
                "model_id": 1141
            },
            {
                "videoid": 2365,
                "model_id": 1141
            },
            {
                "videoid": 2799,
                "model_id": 1141
            },
            {
                "videoid": 2985,
                "model_id": 1141
            },
            {
                "videoid": 3258,
                "model_id": 1141
            },
            {
                "videoid": 3260,
                "model_id": 1141
            },
            {
                "videoid": 3263,
                "model_id": 1141
            },
            {
                "videoid": 3377,
                "model_id": 1141
            },
            {
                "videoid": 3397,
                "model_id": 1141
            },
            {
                "videoid": 3401,
                "model_id": 1141
            },
            {
                "videoid": 3429,
                "model_id": 1141
            },
            {
                "videoid": 3432,
                "model_id": 1141
            },
            {
                "videoid": 3480,
                "model_id": 1141
            },
            {
                "videoid": 3487,
                "model_id": 1141
            },
            {
                "videoid": 3493,
                "model_id": 1141
            },
            {
                "videoid": 3495,
                "model_id": 1141
            },
            {
                "videoid": 3512,
                "model_id": 1141
            },
            {
                "videoid": 3544,
                "model_id": 1141
            },
            {
                "videoid": 3571,
                "model_id": 1141
            },
            {
                "videoid": 3581,
                "model_id": 1141
            },
            {
                "videoid": 3609,
                "model_id": 1141
            },
            {
                "videoid": 3626,
                "model_id": 1141
            },
            {
                "videoid": 3661,
                "model_id": 1141
            },
            {
                "videoid": 3680,
                "model_id": 1141
            },
            {
                "videoid": 3698,
                "model_id": 1141
            },
            {
                "videoid": 3733,
                "model_id": 1141
            },
            {
                "videoid": 4286,
                "model_id": 1141
            },
            {
                "videoid": 4299,
                "model_id": 1141
            },
            {
                "videoid": 4327,
                "model_id": 1141
            },
            {
                "videoid": 4357,
                "model_id": 1141
            },
            {
                "videoid": 4360,
                "model_id": 1141
            },
            {
                "videoid": 4361,
                "model_id": 1141
            },
            {
                "videoid": 4369,
                "model_id": 1141
            },
            {
                "videoid": 4372,
                "model_id": 1141
            },
            {
                "videoid": 4373,
                "model_id": 1141
            },
            {
                "videoid": 1150,
                "model_id": 1100
            },
            {
                "videoid": 1155,
                "model_id": 1100
            },
            {
                "videoid": 1264,
                "model_id": 1100
            },
            {
                "videoid": 1355,
                "model_id": 1100
            },
            {
                "videoid": 1356,
                "model_id": 1100
            },
            {
                "videoid": 1509,
                "model_id": 1100
            },
            {
                "videoid": 1552,
                "model_id": 1100
            },
            {
                "videoid": 1812,
                "model_id": 1100
            },
            {
                "videoid": 1830,
                "model_id": 1100
            },
            {
                "videoid": 1941,
                "model_id": 1100
            },
            {
                "videoid": 2327,
                "model_id": 1100
            },
            {
                "videoid": 2345,
                "model_id": 1100
            },
            {
                "videoid": 2620,
                "model_id": 1100
            },
            {
                "videoid": 3001,
                "model_id": 1100
            },
            {
                "videoid": 3277,
                "model_id": 1100
            },
            {
                "videoid": 3367,
                "model_id": 1100
            },
            {
                "videoid": 3486,
                "model_id": 1100
            },
            {
                "videoid": 3536,
                "model_id": 1100
            },
            {
                "videoid": 3540,
                "model_id": 1100
            },
            {
                "videoid": 3672,
                "model_id": 1100
            },
            {
                "videoid": 3722,
                "model_id": 1100
            },
            {
                "videoid": 4392,
                "model_id": 1100
            },
            {
                "videoid": 4395,
                "model_id": 1100
            },
            {
                "videoid": 4409,
                "model_id": 1100
            },
            {
                "videoid": 4411,
                "model_id": 1100
            },
            {
                "videoid": 4415,
                "model_id": 1100
            },
            {
                "videoid": 4417,
                "model_id": 1100
            },
            {
                "videoid": 4427,
                "model_id": 1100
            },
            {
                "videoid": 4429,
                "model_id": 1100
            },
            {
                "videoid": 4432,
                "model_id": 1100
            },
            {
                "videoid": 4437,
                "model_id": 1100
            },
            {
                "videoid": 1215,
                "model_id": 1382
            },
            {
                "videoid": 1237,
                "model_id": 1382
            },
            {
                "videoid": 1702,
                "model_id": 1382
            },
            {
                "videoid": 1726,
                "model_id": 1382
            },
            {
                "videoid": 1748,
                "model_id": 1382
            },
            {
                "videoid": 1902,
                "model_id": 1382
            },
            {
                "videoid": 1903,
                "model_id": 1382
            },
            {
                "videoid": 2022,
                "model_id": 1382
            },
            {
                "videoid": 2082,
                "model_id": 1382
            },
            {
                "videoid": 2313,
                "model_id": 1382
            },
            {
                "videoid": 2381,
                "model_id": 1382
            },
            {
                "videoid": 2567,
                "model_id": 1382
            },
            {
                "videoid": 2588,
                "model_id": 1382
            },
            {
                "videoid": 3103,
                "model_id": 1382
            },
            {
                "videoid": 3266,
                "model_id": 1382
            },
            {
                "videoid": 3494,
                "model_id": 1382
            },
            {
                "videoid": 4075,
                "model_id": 1382
            },
            {
                "videoid": 4093,
                "model_id": 1382
            },
            {
                "videoid": 4108,
                "model_id": 1382
            },
            {
                "videoid": 4115,
                "model_id": 1382
            },
            {
                "videoid": 4131,
                "model_id": 1382
            },
            {
                "videoid": 4152,
                "model_id": 1382
            },
            {
                "videoid": 4155,
                "model_id": 1382
            },
            {
                "videoid": 4175,
                "model_id": 1382
            },
            {
                "videoid": 4213,
                "model_id": 1382
            },
            {
                "videoid": 4215,
                "model_id": 1382
            },
            {
                "videoid": 4243,
                "model_id": 1382
            },
            {
                "videoid": 4259,
                "model_id": 1382
            },
            {
                "videoid": 1168,
                "model_id": 1355
            },
            {
                "videoid": 1319,
                "model_id": 1355
            },
            {
                "videoid": 1320,
                "model_id": 1355
            },
            {
                "videoid": 1732,
                "model_id": 1355
            },
            {
                "videoid": 1871,
                "model_id": 1355
            },
            {
                "videoid": 1874,
                "model_id": 1355
            },
            {
                "videoid": 2116,
                "model_id": 1355
            },
            {
                "videoid": 2151,
                "model_id": 1355
            },
            {
                "videoid": 2152,
                "model_id": 1355
            },
            {
                "videoid": 2318,
                "model_id": 1355
            },
            {
                "videoid": 2436,
                "model_id": 1355
            },
            {
                "videoid": 2705,
                "model_id": 1355
            },
            {
                "videoid": 2706,
                "model_id": 1355
            },
            {
                "videoid": 2711,
                "model_id": 1355
            },
            {
                "videoid": 2804,
                "model_id": 1355
            },
            {
                "videoid": 3753,
                "model_id": 1355
            },
            {
                "videoid": 3757,
                "model_id": 1355
            },
            {
                "videoid": 3764,
                "model_id": 1355
            },
            {
                "videoid": 3766,
                "model_id": 1355
            },
            {
                "videoid": 3794,
                "model_id": 1355
            },
            {
                "videoid": 3801,
                "model_id": 1355
            },
            {
                "videoid": 3823,
                "model_id": 1355
            },
            {
                "videoid": 3827,
                "model_id": 1355
            },
            {
                "videoid": 3838,
                "model_id": 1355
            },
            {
                "videoid": 3842,
                "model_id": 1355
            },
            {
                "videoid": 1203,
                "model_id": 1107
            },
            {
                "videoid": 1231,
                "model_id": 1107
            },
            {
                "videoid": 1368,
                "model_id": 1107
            },
            {
                "videoid": 1707,
                "model_id": 1107
            },
            {
                "videoid": 1786,
                "model_id": 1107
            },
            {
                "videoid": 2119,
                "model_id": 1107
            },
            {
                "videoid": 2488,
                "model_id": 1107
            },
            {
                "videoid": 2577,
                "model_id": 1107
            },
            {
                "videoid": 2636,
                "model_id": 1107
            },
            {
                "videoid": 2665,
                "model_id": 1107
            },
            {
                "videoid": 2806,
                "model_id": 1107
            },
            {
                "videoid": 2878,
                "model_id": 1107
            },
            {
                "videoid": 3076,
                "model_id": 1107
            },
            {
                "videoid": 3111,
                "model_id": 1107
            },
            {
                "videoid": 3163,
                "model_id": 1107
            },
            {
                "videoid": 3379,
                "model_id": 1107
            },
            {
                "videoid": 3436,
                "model_id": 1107
            },
            {
                "videoid": 3545,
                "model_id": 1107
            },
            {
                "videoid": 3643,
                "model_id": 1107
            },
            {
                "videoid": 3673,
                "model_id": 1107
            },
            {
                "videoid": 3677,
                "model_id": 1107
            },
            {
                "videoid": 3726,
                "model_id": 1107
            }
        ]

# File to store the processed model IDs
response_file = 'model_video_response_june_11_2025.json'
processed_ids_file = "model_processed_june_11_2025.json"



# Load the processed IDs from the file, if it exists
if os.path.exists(response_file):
    with open(response_file, 'r') as f:
        processed_data = json.load(f)
else:
    processed_data = []

# Function to save the processed IDs to a JSON file
def save_processed_data():
    with open(response_file, 'w') as f:
        json.dump(processed_data, f)

if os.path.exists(processed_ids_file):
    with open(processed_ids_file, 'r') as f:
        processed_ids = json.load(f)
else:
    processed_ids = []

# Function to save the processed IDs to a JSON file
def save_processed_ids():
    with open(processed_ids_file, 'w') as f:
        json.dump(processed_ids, f)

# Function to process a model video ID
def process_video(model_id):
    # logger.log(logging.INFO,"Started processing video : "+str(model_id))
    # Step 2: Fetch model video data from the API
    url = f'{PROD}/api/v1/model-video/{model_id}'  # FOR MODEL VIDEO
    # url = f'{PROD}/api/v1/model/{model_id}'  # FOR MODELs

    headers = {
        'sec-ch-ua-platform': 'macOS',
        'Authorization': f'Bearer {TOKEN_PROD}',
        'Referer': 'https://mosaic-dev.24c.in/',
        'tenantId': 'ef7534de-931e-4c68-932e-626da1092f29',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'ngrok-skip-browser-warning': '69420',
        'role': 'PUBLISHER',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*'
    }

    response = requests.get(url, headers=headers)
    logger.log(logging.INFO,"Prod API Hit")


    if response.status_code == 200:
        data = response.json()["data"]
        youtube_url = data["url"] # FOR MODEL-VIDEO
        categories = data['categories']  # FOR MDOEL - VIDEO
        # youtube_url = data['featureVideoURL'] # FOR MDOEL
        # categories = []                       # FOR MDOEL


        logger.log(logging.INFO, youtube_url)
        needGif, needVideo = False, False
        # Model VIDEO case
        if "featureVideoURL" in data.keys() and data["featureVideoURL"] != None:
            needGif = "bikeGifId" in data and data["bikeGifId"] is None
            needVideo = "previewVideoId" in data and data["previewVideoId"] is None

            if needVideo or needGif:
                logger.log(logging.INFO,
                           f"Need video/gif creation for model-id : {model_id}, needVideo : {needVideo}, needGif : {needGif}")

                star_time = time.time()
                logger.log(logging.INFO, msg=f"Hit_download :=> {youtube_url}")
                download_response = downloadYoutubeVideo.check_video_exists_on_s3(youtube_url, "cdn.cars24.com")
                if download_response == None:
                    download_response = downloadYoutubeVideo.downloadAndUploadToS3(youtube_url, "downloads",
                                                                                   "cdn.cars24.com")
                else:
                    logger.log(logging.INFO, msg=f"Video already present in S3 : {download_response}")

                response_data = dict()
                process_video_url = "http://13.200.213.33:80/process-videov2"
                time_data = [{"startTime": data['featureVideoStartTime'], "endTime": data['featureVideoEndTime']}]
                output_url = download_response['body']['s3url']
                process_data = {
                    "time": time_data,
                    "url": output_url,
                    "modelName": data['name'],
                    "makeName": data['make']["name"],
                    "videoName": download_response["body"]["fileName"],
                    "mp4Flag": True,
                    "serverType": serverType,
                    "productType":"bikes24"
                }
                if needVideo:

                    start_time = time.time()
                    logger.log(logging.INFO,
                               f"Hitting video-generation api with time-delta : {process_data['time']}")
                    process_video_response = requests.post(process_video_url, json=process_data, headers={
                        'authorization': f'Bearer {TOKEN_PROD}',
                        'content-type': 'application/json',
                        'tenantid': 'ef7534de-931e-4c68-932e-626da1092f29',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                    })
                    end_time = time.time()
                    elapsed_time = end_time - star_time
                    logger.log(logging.INFO, f"Video-processing :=> time-taken : {elapsed_time:.2f}")
                    logger.log(logging.INFO, f"Video - respose from node server : {process_video_response}")
                    logger.log(logging.INFO,
                               f'response from node for Video-processing : {process_video_response.json()}')

                    if process_video_response.status_code == 200:
                        response_data["modelId"] = model_id
                        response_data["videoId"] = process_video_response.json()["data"]["data"]["id"]
                        logger.log(logging.INFO,
                                   f"response from node (VIDEO): modelId :{model_id}, response : {process_video_response.json()}")

                        processed_data.append(response_data)
                    else:
                        logger.log(logging.WARN,
                                   f"response from node (VIDEO): modelId :{model_id}, response : {process_video_response.json()}")
                else:
                    logger.log(logging.WARN,
                               f"Skipping video creation for model-id : {model_id}")

                if needGif:

                    process_data["mp4Flag"] = False

                    logger.log(logging.INFO, f"Hitting gif-generation api with meta-data : {process_data}")
                    start_time = time.time()
                    process_video_response = requests.post(process_video_url, json=process_data, headers={
                        'authorization': f'Bearer {TOKEN_PROD}',
                        'content-type': 'application/json',
                        'tenantid': 'ef7534de-931e-4c68-932e-626da1092f29',
                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                    })
                    end_time = time.time()
                    elapsed_time = end_time - star_time
                    logger.log(logging.INFO, f"Gif-processing :=> time taken: {elapsed_time:.2f}s")
                    logger.log(logging.INFO, f"GIF - respose from node server : {process_video_response}")
                    logger.log(logging.INFO, f'response from node for Gif-processing : {process_video_response.json()}')

                    if process_video_response.status_code == 200:
                        # Mark the ID as processed
                        response_data["modelId"] = model_id
                        response_data["gifId"] = process_video_response.json()["data"]["data"]["id"]
                        logger.log(logging.INFO,
                                   f"response from node (VIDEO): modelId :{model_id}, response : {process_video_response.json()}")

                        processed_data.append(response_data)
                    else:
                        logger.log(logging.WARN,
                                   f"response from node (VIDEO): modelId :{model_id}, response : {process_video_response.json()}")
                else:
                    logger.log(logging.WARN,
                               f"Skipping gif creation for model-id : {model_id}")

                if (len(response_data) > 0):
                    processed_data.append(response_data)
                    save_processed_data()
            save_processed_ids()
            return

        #  ONLY IN THE CASE OF MODEL-VIDEO
        needVideo = False
        needGif = False
        for category in categories:
            category_id = category["id"]
            print(f"categorieID : {category_id}")
            needVideo = category["videoId"] is None
            needGif = category["gifId"] is None

            if needVideo or needGif:
                logger.log(logging.INFO,
                           f"Need video/gif creation for model-id : {model_id} and categoryId : {category_id}, needVideo : {needVideo}, needGif : {needGif}")

                break
            else:
                if (needVideo or needGif)==False:
                    logger.log(logging.INFO,
                               f"Skipping video/gif creation for model-id : {model_id} and categoryId : {category_id}")
                    return



        star_time = time.time()
        logger.log(logging.INFO,msg=f"Hit_download :=> {youtube_url}")
        download_response = downloadYoutubeVideo.check_video_exists_on_s3(youtube_url, "cdn.cars24.com")
        if download_response == None:
            download_response = downloadYoutubeVideo.downloadAndUploadToS3(youtube_url, "downloads", "cdn.cars24.com")
        else:
            logger.log(logging.INFO, msg=f"Video already present in S3 : {download_response}")
        if download_response.get("status") == 200:
            for _ in range(1000):
                try:
                    if True:
                        job_status_data = download_response
                        if job_status_data['status'] == 200 and download_response['body']['s3url']:
                            output_url = download_response['body']['s3url']

                            # Step 5: Process the video URL with the final API
                            process_video_url = "http://13.200.213.33:80/process-videov2"
                            elapsed_time = time.time() - star_time
                            logger.log(logging.INFO, msg=f"download-time {elapsed_time:.2f}s")

                            # logger.log(logging.INFO, str(categories))
                            for category in categories:
                                category_id = category["id"]
                                print(f"categorieID : {category_id}")
                                needVideo = category["videoId"] is None
                                needGif   = category["gifId"] is None

                                if category["startTime"] == None or category["endTime"] == None:
                                    response_data = dict()
                                    response_data["categoriesId"] = category_id
                                    response_data["gifId"] = None
                                    response_data["videoId"] = None
                                    processed_data.append(response_data)
                                    save_processed_data()
                                    continue
                                process_video_response = None
                                response_data = dict()
                                time_data = [{"startTime": category['startTime'], "endTime": category['endTime']}]
                                process_data = {
                                    "time": time_data,
                                    "url": output_url,
                                    "modelName": data['model']['name'],
                                    "makeName": data['model']['make']['name'],
                                    "videoName": data['name'],
                                    "mp4Flag": True,
                                    "serverType": serverType,
                                    "categoryId": category_id,
                                    "productType":"bikes24" # For cars: "newcars", bikes: "bikes24"
                                }

                                if needVideo:

                                    logger.log(logging.INFO,f"Hitting video-generation api for categoryId : {category_id}, with time-delta : {process_data['time']}")
                                    start_time =  time.time()
                                    process_video_response = requests.post(process_video_url, json=process_data, headers={
                                        'authorization': f'Bearer {TOKEN_PROD}',
                                        'content-type': 'application/json',
                                        'tenantid': 'ef7534de-931e-4c68-932e-626da1092f29',
                                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                                    })
                                    end_time =  time.time()
                                    elapsed_time = end_time-star_time
                                    logger.log(logging.INFO,f"Video-processing :=> time-taken : {elapsed_time:.2f}")
                                    logger.log(logging.INFO, f"Video - respose from node server : {process_video_response}")
                                    logger.log(logging.INFO,f'response from node for Video-processing : {process_video_response.json()}')

                                    if process_video_response.status_code == 200:
                                        response_data["categoriesId"] = category["id"]
                                        response_data["videoId"] = process_video_response.json()["data"]["data"]["id"]
                                        logger.log(logging.INFO,
                                                   f"response from node (VIDEO): modelId :{model_id}, categoryId : {category_id}, response : {process_video_response.json()}")

                                    else:
                                        logger.log(logging.WARN,
                                                   f"response from node (VIDEO): modelId :{model_id}, categoryId : {category_id}, response : {process_video_response.json()}")
                                else:
                                    logger.log(logging.WARN,f"Skipping video creation for model-id : {model_id} and categoryId : {category_id}")

                                if needGif:

                                    process_data["mp4Flag"] = False

                                    logger.log(logging.INFO,f"Hitting gif-generation api with meta-data : {process_data}")
                                    start_time =  time.time()
                                    process_video_response = requests.post(process_video_url, json=process_data, headers={
                                        'authorization': f'Bearer {TOKEN_PROD}',
                                        'content-type': 'application/json',
                                        'tenantid': 'ef7534de-931e-4c68-932e-626da1092f29',
                                        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                                    })
                                    end_time =  time.time()
                                    elapsed_time  = end_time-star_time
                                    logger.log(logging.INFO,f"Gif-processing :=> time taken: {elapsed_time:.2f}s")
                                    logger.log(logging.INFO, f"GIF - respose from node server : {process_video_response}")
                                    logger.log(logging.INFO,f'response from node for Gif-processing : {process_video_response.json()}')

                                    if process_video_response.status_code == 200:
                                        # Mark the ID as processed
                                        response_data["categoriesId"] = category["id"]
                                        response_data["gifId"] = process_video_response.json()["data"]["data"]["id"]
                                        logger.log(logging.INFO,
                                                   f"response from node (VIDEO): modelId :{model_id}, categoryId : {category_id}, response : {process_video_response.json()}")
                                    else:
                                        logger.log(logging.WARN,
                                               f"response from node (VIDEO): modelId :{model_id}, categoryId : {category_id}, response : {process_video_response.json()}")
                                else:
                                    logger.log(logging.WARN,f"Skipping gif creation for model-id : {model_id} and categoryId : {category_id}")

                                if(len(response_data)>0):
                                    processed_data.append(response_data)
                                    save_processed_data()

                            processed_ids.append(model_id)
                            save_processed_ids()

                        else:
                            continue
                    else:
                        print(f"Polling failed for job {job_id}")
                        continue
                except Exception as e:
                    e.with_traceback()
                    logger.log(logging.ERROR, msg=f"Failed to process for model_id {model_id}, error : {e}")
                break
        else:
            logger.log(logging.ERROR, msg=f"Failed to trigger download for model {model_id}")
    else:
        logger.log(logging.ERROR, msg=f"Failed to fetch model video for ID {model_id}, status: {response.status_code}, error : {response.content}")

# long_time_taking_model_ids = [2,18,24, 33, 34,42]
# 34 -> start, end time = 0,0
long_time_taking_model_ids = []

for _model_id_ in video_id_lst[::-1]:
# for _model_id_ in model_id_lst:

    model_id = _model_id_["videoid"]
    # model_id = _model_id_["id"] # FOR MODEL ONLY
    if model_id not in processed_ids:
        s_t =  time.time()
        logger.log(logging.INFO,f"Processing for Video ID {model_id}")
        # logger.log(logging.INFO,f"Processing for Model ID {model_id}")
        try:
            process_video(model_id)
            processed_ids.append(model_id)
        except Exception as e:
            traceback.print_exc()
            logger.log(logging.ERROR,f'error while handling for video id : {model_id}, error  : {e}')
            # logger.log(logging.ERROR,f'error while handling for model id : {model_id}, error  : {e}')

        end_time =  time.time()
        elapsed_time = end_time - s_t
        logger.log(logging.INFO, f"Time taken to process video-id {model_id}: {elapsed_time:.2f}s")
        # logger.log(logging.INFO, f"Time taken to process model-id {model_id}: {elapsed_time:.2f}s")

    else:
        print(f"Video ID {model_id} has already been processed.")
        # print(f"Model ID {model_id} has already been processed.")
