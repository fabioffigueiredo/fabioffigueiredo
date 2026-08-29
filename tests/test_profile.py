from __future__ import annotations

import hashlib
import json
import re
import struct
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
MANIFEST = ROOT / "assets" / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:24]
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"{path} is not a PNG")
    return struct.unpack(">II", data[16:24])


def gif_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()[:10]
    if data[:6] not in {b"GIF87a", b"GIF89a"}:
        raise AssertionError(f"{path} is not a GIF")
    return struct.unpack("<HH", data[6:10])


class ProfileReadmeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.readme = README.read_text(encoding="utf-8")
        cls.manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def test_name_has_no_accent(self) -> None:
        self.assertIn("# Fabio Figueiredo", self.readme)
        self.assertNotIn("Fábio", self.readme)

    def test_forbidden_claims_and_widgets_are_absent(self) -> None:
        forbidden = (
            "AI FIRST",
            "92% acurácia",
            "100+ pessoas",
            "Kubernetes & MLOps Expert",
            "readme-typing-svg",
            "github-readme-stats",
            "profile-views",
            "github-profile-trophy",
            "streak-stats",
        )
        for value in forbidden:
            self.assertNotIn(value.casefold(), self.readme.casefold())

    def test_public_images_are_local_and_have_alt_text(self) -> None:
        images = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", self.readme)
        self.assertEqual(4, len(images))
        for alt, target in images:
            self.assertGreaterEqual(len(alt.strip()), 24)
            self.assertFalse(target.startswith(("http://", "https://")))
            self.assertTrue((ROOT / target).is_file(), target)

    def test_manifest_hashes_match_assets(self) -> None:
        for item in self.manifest["assets"]:
            path = ROOT / item["path"]
            self.assertTrue(path.is_file(), item["path"])
            self.assertEqual(item["sha256"], sha256(path), item["path"])
        for item in self.manifest["fonts"]:
            path = ROOT / item["path"]
            self.assertTrue(path.is_file(), item["path"])
            self.assertEqual(item["sha256"], sha256(path), item["path"])
            self.assertTrue((ROOT / item["license_path"]).is_file())

    def test_banner_contract(self) -> None:
        path = ROOT / "assets" / "profile-hero.png"
        self.assertEqual((1280, 384), png_dimensions(path))
        self.assertLess(path.stat().st_size, 1_000_000)

    def test_animation_contract(self) -> None:
        path = ROOT / "assets" / "visionops-tracking.gif"
        data = path.read_bytes()
        self.assertEqual((960, 540), gif_dimensions(path))
        self.assertLess(path.stat().st_size, 5_000_000)
        self.assertNotIn(b"NETSCAPE2.0", data)
        self.assertNotIn(b"ANIMEXTS1.0", data)

    def test_readme_has_no_em_dash(self) -> None:
        self.assertNotIn("—", self.readme)

    def test_mlops_block_uses_the_versioned_blocked_gate_evidence(self) -> None:
        commit = "1ada3456dd7c905498505adb619d1632bc169d46"
        normalized_readme = re.sub(r"\s+", " ", self.readme).casefold()
        required = (
            "Recall +0,0559",
            "Precision -0,0298",
            "FP +405",
            "FN -112",
            "custo de falso positivo",
            "custo de falso negativo",
            "threshold escolhido",
            "validação temporal",
            "plano de monitoramento",
        )

        self.assertGreaterEqual(self.readme.count(commit), 2)
        self.assertIn("assets/mlops-promotion-gate.png", self.readme)
        self.assertNotIn("assets/mlops-experiment-tracking.png", self.readme)
        self.assertNotIn("tree/9358182", self.readme)
        self.assertLess(
            normalized_readme.index("a função desta interface"),
            normalized_readme.index("a arquitetura conecta"),
        )
        for value in required:
            self.assertIn(value.casefold(), normalized_readme)

    def test_mlops_manifest_records_real_blocked_gate_provenance(self) -> None:
        item = next(
            asset
            for asset in self.manifest["assets"]
            if asset["path"] == "assets/mlops-promotion-gate.png"
        )

        self.assertEqual("blocked", item["promotion_gate"])
        self.assertEqual(
            "1ada3456dd7c905498505adb619d1632bc169d46",
            item["source_commit"],
        )
        self.assertFalse(item["synthetic_media"])
        self.assertEqual(
            [
                "false_positive_cost",
                "false_negative_cost",
                "threshold",
                "temporal_validation",
                "monitoring",
            ],
            item["missing_evidence"],
        )


if __name__ == "__main__":
    unittest.main()
