var treeJson = [
  {
    name: "Software Development",
    value: 14,
    type: "black",
    level: "red",
    children: [
      {
        name: "Software Engineer",
        parent: "Software Development",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "C++",
            parent: "Software Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "C++",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SQL",
            parent: "Software Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SQL",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "React",
            parent: "Software Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "React",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Agile",
            parent: "Software Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Agile",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Design Patterns",
            parent: "Software Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Design Patterns",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
        ],
      },
      {
        name: "Software Developer",
        parent: "Software Development",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "SQL",
            parent: "Software Developer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SQL",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "CSS",
            parent: "Software Developer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "CSS",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Azure",
            parent: "Software Developer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Azure",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "React",
            parent: "Software Developer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "React",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "REST",
            parent: "Software Developer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "REST",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
        ],
      },
      {
        name: "DevOps Engineer",
        parent: "Software Development",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "DevOps",
            parent: "DevOps Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "DevOps",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Azure",
            parent: "DevOps Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Azure",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Shell Scripting",
            parent: "DevOps Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Shell Scripting",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Bash",
            parent: "DevOps Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Bash",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Jenkins",
            parent: "DevOps Engineer",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Jenkins",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
        ],
      },
    ],
  },
];
console.log(JSON.parse(treeJson));
