{
    ["Your Cut"] = {
    	["id"]                  = 3400,
        ["tier"]                = 1,
        ["type"]                = {"Distributed"},
        ["limit"]               = "Only granted by {{cai|Death from Below|Pyke}}.",
        ["modes"] = {
            ["classic sr 5v5"]  = true,
            ["aram"]            = true,
            ["nb"]              = true,
            ["arena"]           = true,
        },
        ["effects"] = {
            ["consume"]         = "Grants {{g|text=*none*}}{{pp|100;112;140;176;220;274;300|-7+x;0+|type=target's kill bounty|color=gold}}, increased by {{g|100}} for [[First Blood]]. '''Can be used while [[death|dead]].'''",
        },
    },
    ["Abyssal Mask"] = {
        ["id"]                  = 8020,
        ["tier"]                = 3,
        ["type"]                = {"Legendary"},
        ["modes"] = {
            ["classic sr 5v5"]  = true,
            ["aram"]            = true,
            ["nb"]              = true,
            ["arena"]           = true,
        },
        ["menu"] = {
            ["tank"]            = true,
        },
        ["stats"] = {
            ["ah"]              = 10,
            ["hp"]              = 300,
            ["mr"]              = 60,
        },
        ["effects"] = {
            ["pass"] = {
                ["name"]        = "Unmake",
                ["unique"]      = true,
                ["description"] = "Enemy champions within {{tt|550 units|center to edge}} of you become cursed, reducing their {{as|magic resistance by 5}} {{as|(+ {{fd|1.2}}% '''bonus''' health)}}, capped at a reduction of {{as|25|magic resistance}}. Gain {{as|9 '''bonus''' magic resistance}} per cursed enemy.",
            },
        },
        ["recipe"]              = {"Kindlegem", "Negatron Cloak"},
        ["buy"]                 = 2400,
    }
}