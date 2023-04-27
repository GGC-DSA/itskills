var treeJson = [
  {
    name: "Data Science and Analytics",
    value: 14,
    type: "black",
    level: "red",
    children: [
      {
        name: "Data Scientist",
        parent: "Data Science and Analytics",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "Python",
            parent: "Data Scientist",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Python",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Machine Learning",
            parent: "Data Scientist",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Machine Learning",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SQL",
            parent: "Data Scientist",
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
            name: "R",
            parent: "Data Scientist",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "R",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Data Mining",
            parent: "Data Scientist",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Data Mining",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
        ],
      },
      {
        name: "Data Analyst",
        parent: "Data Science and Analytics",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "Python",
            parent: "Data Analyst",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Python",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Machine Learning",
            parent: "Data Analyst",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Machine Learning",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SQL",
            parent: "Data Analyst",
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
            name: "R",
            parent: "Data Analyst",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "R",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Analysis Skills",
            parent: "Data Analyst",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Analysis Skills",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
        ],
      },
      {
        name: "Data Architect",
        parent: "Data Science and Analytics",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "Machine Learning",
            parent: "Data Architect",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Machine Learning",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "Python",
            parent: "Data Architect",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "Python",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "AI",
            parent: "Data Architect",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "AI",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "PyTorch",
            parent: "Data Architect",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "PyTorch",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "TensorFlow",
            parent: "Data Architect",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "TensorFlow",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
        ],
      },
      {
        name: "JOB 4",
        parent: "Data Science and Analytics",
        value: 12,
        type: "grey",
        level: "pink",
        _children: [
          {
            name: "SKILL 1",
            parent: "JOB 4",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SKILL 1",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SKILL 2",
            parent: "JOB 4",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SKILL 2",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SKILL 3",
            parent: "JOB 4",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SKILL 3",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SKILL 4",
            parent: "JOB 4",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SKILL 4",
                value: 9,
                type: "darkblue",
                level: "purple",
              },
            ],
          },
          {
            name: "SKILL 5",
            parent: "JOB 4",
            value: 10,
            type: "steelblue",
            level: "green",
            _children: [
              {
                name: "COURSE",
                parent: "SKILL 5",
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
