import requests
from jinja2 import Environment, FileSystemLoader

# Placeholder access tokens - replace with real credentials
FB_TOKEN = "YOUR_FACEBOOK_TOKEN"
IG_TOKEN = "YOUR_INSTAGRAM_TOKEN"
LINKEDIN_TOKEN = "YOUR_LINKEDIN_TOKEN"


def get_facebook_data():
    """Fetch metrics from Facebook Graph API (sample)."""
    url = "https://graph.facebook.com/v18.0/me/insights"
    params = {"access_token": FB_TOKEN}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}


def get_instagram_data():
    url = "https://graph.facebook.com/v18.0/me?fields=followers_count"
    params = {"access_token": IG_TOKEN}
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}


def get_linkedin_posts():
    url = "https://api.linkedin.com/v2/ugcPosts"
    headers = {"Authorization": f"Bearer {LINKEDIN_TOKEN}"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception:
        return {}


def main():
    # Collect data from APIs
    fb_data = get_facebook_data()
    ig_data = get_instagram_data()
    li_posts = get_linkedin_posts()

    # Example metrics from the prompt
    dashboard = {
        "date_range": "3/9/2025 - 6/6/2025",
        "impressions": 11004,
        "members_reached": 4797,
        "linkedin_posts": [
            {
                "url": "https://www.linkedin.com/feed/update/urn:li:share:7326839399520894976",
                "date": "May 14, 2025",
                "time": "9:00 PM",
                "impressions": 2162,
                "members_reached": 1574,
                "reactions": 38,
                "comments": 4,
                "reposts": 1,
                "top_react_job": "Retail Consultant",
                "top_react_location": "New York City Metropolitan Area",
                "top_react_industry": "Retail Apparel and Fashion",
                "top_comment_job": "Design Specialist",
                "top_comment_location": "New York City Metropolitan Area",
                "top_comment_industry": "Retail Apparel and Fashion",
            },
            {
                "url": "https://www.linkedin.com/feed/update/urn:li:ugcPost:7328937325730713601",
                "date": "May 16, 2025",
                "time": "12:20 AM",
                "impressions": 975,
                "members_reached": 684,
                "reactions": 15,
                "comments": 7,
                "reposts": None,
                "top_react_job": "Account Manager",
                "top_react_location": "New York City Metropolitan Area",
                "top_react_industry": "Higher Education",
                "top_comment_job": "Dental Assisting Instructor",
                "top_comment_location": "New York City Metropolitan Area",
                "top_comment_industry": "Retail Apparel and Fashion",
            },
            {
                "url": "https://www.linkedin.com/feed/update/urn:li:share:7326841046334615552",
                "date": "May 14, 2025",
                "time": "5:30 PM",
                "impressions": 663,
                "members_reached": 458,
                "reactions": 11,
                "comments": 10,
                "reposts": 1,
                "top_react_job": "Technology Technician",
                "top_react_location": "Greater Melbourne Area",
                "top_react_industry": "Retail Apparel and Fashion",
                "top_comment_job": "Research Assistant",
                "top_comment_location": "Greater Melbourne Area",
                "top_comment_industry": "Retail Apparel and Fashion",
            },
        ],
    }

    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("kpi_dashboard_template.html")
    rendered = template.render(**dashboard)

    with open("KPI_Dashboard.html", "w", encoding="utf-8") as f:
        f.write(rendered)

    print("KPI dashboard generated -> KPI_Dashboard.html")


if __name__ == "__main__":
    main()
