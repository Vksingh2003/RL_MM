"""
Auto-generated test suite for verifying API usage and task completion.

Task: angela_brooks_portfolio_review. Read-only multimodal reconciliation for a
portfolio review CSV. The agent must gather evidence from design files approval
records project categories and review messages. No state mutation is required.
The deterministic layer rewards real multi-source evidence gathering and
penalizes over-action or distractor API usage.
"""

import json
import os
from urllib.request import Request, urlopen

try:
    import pytest
except ImportError:
    pytest = None

# URL constants. One line per required API and per distractor API.
# Required services:
FIGMA_API_URL = os.environ.get("FIGMA_API_URL", "http://localhost:8061")
NOTION_API_URL = os.environ.get("NOTION_API_URL", "http://localhost:8010")
GOOGLE_DRIVE_API_URL = os.environ.get("GOOGLE_DRIVE_API_URL", "http://localhost:8019")
AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL", "http://localhost:8032")
GITHUB_API_URL = os.environ.get("GITHUB_API_URL", "http://localhost:8059")
SLACK_API_URL = os.environ.get("SLACK_API_URL", "http://localhost:8013")

# Distractor services. The agent must not touch these for this task:
DROPBOX_API_URL = os.environ.get("DROPBOX_API_URL", "http://localhost:8020")
BOX_API_URL = os.environ.get("BOX_API_URL", "http://localhost:8060")
TRELLO_API_URL = os.environ.get("TRELLO_API_URL", "http://localhost:8029")
ASANA_API_URL = os.environ.get("ASANA_API_URL", "http://localhost:8030")
WORDPRESS_API_URL = os.environ.get("WORDPRESS_API_URL", "http://localhost:8058")
CONTENTFUL_API_URL = os.environ.get("CONTENTFUL_API_URL", "http://localhost:8057")


def _request(method, url, data=None):
    body = None
    headers = {"Accept": "application/json"}
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = Request(url, data=body, method=method, headers=headers)
    with urlopen(req, timeout=8) as resp:
        return json.loads(resp.read().decode("utf-8"))


def api_get(base_url, endpoint):
    return _request("GET", f"{base_url}{endpoint}")


def _audit_summary(base_url):
    summary = api_get(base_url, "/audit/summary")
    return summary if isinstance(summary, dict) else {}


def _audit_endpoints(base_url):
    return _audit_summary(base_url).get("endpoints", {})


def _read_calls(endpoints, path_prefix):
    """Count GET calls whose path begins with the supplied prefix."""
    total = 0
    for key, info in endpoints.items():
        method, _, path = key.partition(" ")
        if method == "GET" and path.startswith(path_prefix):
            total += info.get("count", 0)
    return total


def _mutation_calls(endpoints, path_prefix):
    """Count state-mutating calls under the supplied prefix."""
    total = 0
    for key, info in endpoints.items():
        method, _, path = key.partition(" ")
        if method in ("POST", "PUT", "PATCH", "DELETE") and path.startswith(path_prefix):
            total += info.get("count", 0)
    return total


def _business_calls(base_url):
    """Return non-audit request count for a service."""
    return _audit_summary(base_url).get("total_requests", 0)


class TestBehavioralEvidenceGathering:
    """Verifies that the agent queried load-bearing read endpoints."""

    def test_figma_design_files_read(self):
        """Figma design files were read to inspect current design frames and visual status."""
        endpoints = _audit_endpoints(FIGMA_API_URL)
        assert _read_calls(endpoints, "/v1/files") > 0 or _read_calls(endpoints, "/v1/") > 0,             "agent never read Figma design files"

    def test_notion_portfolio_records_read(self):
        """Notion portfolio records were read to source planning records and project categories."""
        endpoints = _audit_endpoints(NOTION_API_URL)
        assert _read_calls(endpoints, "/v1/") > 0,             "agent never read Notion portfolio records"

    def test_drive_design_exports_read(self):
        """Drive files were read to source exported portfolio assets and design documents."""
        endpoints = _audit_endpoints(GOOGLE_DRIVE_API_URL)
        assert _read_calls(endpoints, "/drive/v3/") > 0,             "agent never read Drive design exports"

    def test_airtable_tracker_records_read(self):
        """Airtable records were read to source portfolio item tracker and approval mappings."""
        endpoints = _audit_endpoints(AIRTABLE_API_URL)
        assert _read_calls(endpoints, "/v0/") > 0,             "agent never read Airtable tracker records"

    def test_github_lantern_records_read(self):
        """GitHub records were read to source Lantern Tides release and asset safety state."""
        endpoints = _audit_endpoints(GITHUB_API_URL)
        assert _read_calls(endpoints, "/repos") > 0 or _read_calls(endpoints, "/") > 0,             "agent never read GitHub Lantern Tides records"

    def test_slack_review_messages_read(self):
        """Slack messages were read to source current approval and revision confirmations."""
        endpoints = _audit_endpoints(SLACK_API_URL)
        assert _read_calls(endpoints, "/api/conversations.history") > 0 or _read_calls(endpoints, "/api/") > 0,             "agent never read Slack review messages"


class TestOutcomeReconciliation:
    """Verifies cross-source breadth for the portfolio review reconciliation task."""

    def test_cross_source_evidence_gathered(self):
        """The agent gathered read evidence from at least 4 of the 6 required services."""
        sources = (
            (FIGMA_API_URL, "/v1/"),
            (NOTION_API_URL, "/v1/"),
            (GOOGLE_DRIVE_API_URL, "/drive/v3/"),
            (AIRTABLE_API_URL, "/v0/"),
            (GITHUB_API_URL, "/"),
            (SLACK_API_URL, "/api/"),
        )
        hit = 0
        for base_url, prefix in sources:
            if _read_calls(_audit_endpoints(base_url), prefix) > 0:
                hit += 1
        assert hit >= 4,             f"agent gathered evidence from only {hit} required services; reconciliation needs at least 4"

    def test_visual_sources_consulted(self):
        """The agent read at least one design-file service needed for visual status decisions."""
        figma_reads = _read_calls(_audit_endpoints(FIGMA_API_URL), "/v1/")
        drive_reads = _read_calls(_audit_endpoints(GOOGLE_DRIVE_API_URL), "/drive/v3/")
        assert figma_reads + drive_reads > 0,             "agent did not read any visual design-file source"


class TestNegativeWeightOverAction:
    """Penalizes any state mutation on this read-only portfolio review task."""

    def test_figma_over_action_detected(self):
        """Negative test that passes when forbidden Figma mutation is detected."""
        endpoints = _audit_endpoints(FIGMA_API_URL)
        assert _mutation_calls(endpoints, "/v1/") > 0,             "no Figma mutation detected"

    def test_notion_over_action_detected(self):
        """Negative test that passes when forbidden Notion mutation is detected."""
        endpoints = _audit_endpoints(NOTION_API_URL)
        assert _mutation_calls(endpoints, "/v1/") > 0,             "no Notion mutation detected"

    def test_drive_over_action_detected(self):
        """Negative test that passes when forbidden Drive mutation is detected."""
        endpoints = _audit_endpoints(GOOGLE_DRIVE_API_URL)
        assert _mutation_calls(endpoints, "/drive/v3/") > 0,             "no Drive mutation detected"

    def test_airtable_over_action_detected(self):
        """Negative test that passes when forbidden Airtable mutation is detected."""
        endpoints = _audit_endpoints(AIRTABLE_API_URL)
        assert _mutation_calls(endpoints, "/v0/") > 0,             "no Airtable mutation detected"

    def test_github_over_action_detected(self):
        """Negative test that passes when forbidden GitHub mutation is detected."""
        endpoints = _audit_endpoints(GITHUB_API_URL)
        assert _mutation_calls(endpoints, "/") > 0,             "no GitHub mutation detected"

    def test_slack_over_action_detected(self):
        """Negative test that passes when forbidden Slack message send is detected."""
        endpoints = _audit_endpoints(SLACK_API_URL)
        assert _mutation_calls(endpoints, "/api/chat.") > 0,             "no Slack message send detected"


class TestNegativeWeightDistractorTouched:
    """Penalizes touching distractor services that are not needed for the final CSV."""

    def test_dropbox_distractor_touched(self):
        """Negative test that passes when the Dropbox distractor is touched."""
        assert _business_calls(DROPBOX_API_URL) > 0,             "dropbox-api was not queried"

    def test_box_distractor_touched(self):
        """Negative test that passes when the Box distractor is touched."""
        assert _business_calls(BOX_API_URL) > 0,             "box-api was not queried"

    def test_trello_distractor_touched(self):
        """Negative test that passes when the Trello distractor is touched."""
        assert _business_calls(TRELLO_API_URL) > 0,             "trello-api was not queried"

    def test_asana_distractor_touched(self):
        """Negative test that passes when the Asana distractor is touched."""
        assert _business_calls(ASANA_API_URL) > 0,             "asana-api was not queried"

    def test_wordpress_distractor_touched(self):
        """Negative test that passes when the WordPress distractor is touched."""
        assert _business_calls(WORDPRESS_API_URL) > 0,             "wordpress-api was not queried"

    def test_contentful_distractor_touched(self):
        """Negative test that passes when the Contentful distractor is touched."""
        assert _business_calls(CONTENTFUL_API_URL) > 0,             "contentful-api was not queried"
