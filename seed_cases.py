def seed_cases():
    return [
        {
            'id': 1,
            'title': 'Broken Borehole in Zamfara Village',
            'summary': 'Residents of a rural village in Zamfara report that their only borehole is not dispensing water. Community leaders and organizations have exchanged updates on repair plans.',
            'threads': [
                {
                    'title': 'Initial Complaint',
                    'messages': [
                        {'timestamp': '2025-06-01 08:15', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'The borehole in Gidan-Dari village has stopped working completely.'},
                        {'timestamp': '2025-06-01 09:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'Thanks for reporting. Our team will assess the site.'},
                        {'timestamp': '2025-06-02 10:30', 'author': 'Member', 'channel': 'SMS',
                         'text': 'People are fetching from unsafe streams now.'},
                        {'timestamp': '2025-06-02 11:00', 'author': 'Organization', 'channel': 'Transcript',
                         'text': 'Assessment completed. We will provide new pump parts soon.'},
                    ]
                },
                {
                    'title': 'Repairs and Confirmation',
                    'messages': [
                        {'timestamp': '2025-06-03 14:20', 'author': 'Organization', 'channel': 'SMS',
                         'text': 'Pump parts delivered. Installation ongoing.'},
                        {'timestamp': '2025-06-03 15:00', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'Installation complete. Water is flowing again. Thank you!'},
                    ]
                }
            ]
        },
        {
            'id': 2,
            'title': 'Collapsed Bridge in Bayelsa',
            'summary': 'A key bridge connecting two communities in Bayelsa collapsed after heavy rainfall. Case follows the safety alert and action plans.',
            'threads': [
                {
                    'title': 'Safety Alert and First Response',
                    'messages': [
                        {'timestamp': '2025-06-02 07:45', 'author': 'Member', 'channel': 'SMS',
                         'text': 'The wooden bridge to Okolobiri has collapsed. People are stranded.'},
                        {'timestamp': '2025-06-02 08:10', 'author': 'Organization', 'channel': 'Email',
                         'text': 'We are sending engineers to assess.'},
                        {'timestamp': '2025-06-02 16:00', 'author': 'Organization', 'channel': 'Transcript',
                         'text': 'Temporary crossing set up. Permanent fix under budget review.'},
                        {'timestamp': '2025-06-03 09:30', 'author': 'Member', 'channel': 'SMS',
                         'text': 'Thanks. People are using the detour path for now.'},
                    ]
                },
                {
                    'title': 'Funding and Contractor Engagement',
                    'messages': [
                        {'timestamp': '2025-06-04 10:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'State government allocated emergency funds.'},
                        {'timestamp': '2025-06-05 12:00', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'Please ensure contractor begins soon. Rainfall expected again.'},
                    ]
                }
            ]
        },
        {
            'id': 3,
            'title': 'Unpaid Teachers in Local School',
            'summary': 'Teachers at a public school in Osun State have not been paid for three months. PTA and community leaders intervene.',
            'threads': [
                {
                    'title': 'Teacher Complaints',
                    'messages': [
                        {'timestamp': '2025-06-01 07:10', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'We have not received our salaries since March. We cannot continue teaching without pay.'},
                        {'timestamp': '2025-06-01 08:30', 'author': 'Organization', 'channel': 'Email',
                         'text': 'The issue is under review by the local government.'},
                        {'timestamp': '2025-06-02 09:00', 'author': 'Member', 'channel': 'SMS',
                         'text': 'Students are missing classes. We need action urgently.'},
                        {'timestamp': '2025-06-02 10:00', 'author': 'Organization', 'channel': 'Transcript',
                         'text': 'We’ve escalated it to the education commissioner.'},
                    ]
                },
                {
                    'title': 'PTA Mediation',
                    'messages': [
                        {'timestamp': '2025-06-03 12:30', 'author': 'Organization', 'channel': 'SMS',
                         'text': 'PTA has offered emergency stipends.'},
                        {'timestamp': '2025-06-03 14:00', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'Thank you. Teaching will resume while we await salary resolution.'},
                    ]
                }
            ]
        },
        {
            'id': 4,
            'title': 'Electricity Transformer Theft in Kaduna',
            'summary': 'Residents report the theft of a community transformer. The issue is logged, and discussions around security and replacement begin.',
            'threads': [
                {
                    'title': 'Incident Reporting',
                    'messages': [
                        {'timestamp': '2025-06-01 06:00', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'Our transformer at Angwan Rimi was stolen last night.'},
                        {'timestamp': '2025-06-01 08:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'We are working with police and NEPA to investigate.'},
                        {'timestamp': '2025-06-01 11:45', 'author': 'Member', 'channel': 'SMS',
                         'text': 'We have no light and no business activity today.'},
                        {'timestamp': '2025-06-01 13:00', 'author': 'Organization', 'channel': 'Transcript',
                         'text': 'Security patrols will increase. Replacement being discussed.'},
                    ]
                },
                {
                    'title': 'Replacement Planning',
                    'messages': [
                        {'timestamp': '2025-06-02 10:00', 'author': 'Organization', 'channel': 'Email',
                         'text': 'New transformer will arrive in 5 working days.'},
                        {'timestamp': '2025-06-02 12:30', 'author': 'Member', 'channel': 'Transcript',
                         'text': 'Thank you. We will inform residents and prepare security volunteers.'},
                    ]
                }
            ]
        }
    ]
