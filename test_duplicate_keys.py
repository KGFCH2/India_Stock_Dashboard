#!/usr/bin/env python3
"""
Test script to verify duplicate button key fix
"""
import os
import re

def test_duplicate_keys_fix():
    """Test that there are no duplicate button keys"""
    print("🔍 Testing Duplicate Button Keys Fix...")
    
    file_path = "main.py"
    full_path = os.path.join("d:\\Vs Code\\PROJECT\\India_Stock_Dashboard", file_path)
    
    if os.path.exists(full_path):
        print(f"\n📱 Checking {file_path}...")
        
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find all button keys
        key_pattern = r'key=["\']([^"\']+)["\']'
        keys = re.findall(key_pattern, content)
        
        print("\n🔑 FOUND BUTTON KEYS:")
        key_counts = {}
        for key in keys:
            key_counts[key] = key_counts.get(key, 0) + 1
            print(f"   • {key}")
        
        # Check for duplicates
        duplicates = [key for key, count in key_counts.items() if count > 1]
        
        print(f"\n📊 KEY ANALYSIS:")
        print(f"   • Total keys found: {len(keys)}")
        print(f"   • Unique keys: {len(key_counts)}")
        print(f"   • Duplicate keys: {len(duplicates)}")
        
        if duplicates:
            print(f"\n❌ DUPLICATE KEYS FOUND:")
            for key in duplicates:
                print(f"   • {key} (appears {key_counts[key]} times)")
            return False
        else:
            print(f"\n✅ NO DUPLICATE KEYS!")
            
        # Check specific navigation keys
        nav_keys = [key for key in keys if 'nav' in key.lower()]
        print(f"\n🧭 NAVIGATION KEYS:")
        for key in nav_keys:
            print(f"   • {key}")
        
        # Verify the new structure
        expected_top_nav_keys = ['top_nav_analytics', 'top_nav_logout', 'top_nav_theme']
        expected_menu_nav_keys = ['nav_dashboard', 'nav_market', 'nav_portfolio', 'nav_news', 'nav_analytics']
        
        top_nav_found = [key for key in expected_top_nav_keys if key in keys]
        menu_nav_found = [key for key in expected_menu_nav_keys if key in keys]
        
        print(f"\n🎯 KEY STRUCTURE VERIFICATION:")
        print(f"   📊 Top navigation keys: {len(top_nav_found)}/{len(expected_top_nav_keys)}")
        for key in expected_top_nav_keys:
            status = "✅" if key in keys else "❌"
            print(f"      {status} {key}")
        
        print(f"   📋 Menu navigation keys: {len(menu_nav_found)}/{len(expected_menu_nav_keys)}")
        for key in expected_menu_nav_keys:
            status = "✅" if key in keys else "❌"
            print(f"      {status} {key}")
        
        return len(duplicates) == 0

def test_css_updates():
    """Test that CSS has been updated for new keys"""
    print("\n🎨 Testing CSS Updates...")
    
    file_path = "components/ui_components.py"
    full_path = os.path.join("d:\\Vs Code\\PROJECT\\India_Stock_Dashboard", file_path)
    
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for updated CSS selectors
        css_checks = [
            (r'top_nav_', "Updated CSS selector for top navigation"),
            (r'data-testid.*top_nav', "CSS targeting new button keys")
        ]
        
        css_found = 0
        for pattern, description in css_checks:
            if re.search(pattern, content, re.IGNORECASE):
                print(f"   ✅ {description}: Found")
                css_found += 1
            else:
                print(f"   ❌ {description}: Missing")
        
        return css_found == len(css_checks)
    
    return False

if __name__ == "__main__":
    print("🔧 DUPLICATE BUTTON KEYS - FIX VERIFICATION")
    print("=" * 60)
    
    keys_fixed = test_duplicate_keys_fix()
    css_updated = test_css_updates()
    
    print(f"\n🎯 OVERALL RESULTS:")
    print(f"   🔑 Button keys: {'✅ Fixed' if keys_fixed else '❌ Still has issues'}")
    print(f"   🎨 CSS updates: {'✅ Updated' if css_updated else '❌ Needs updating'}")
    
    if keys_fixed and css_updated:
        print("\n🎉 SUCCESS! Duplicate key issue resolved!")
        print("   🚀 Dashboard should now run without errors")
        print("   🧭 Both navigation systems work independently")
        print("   🎨 CSS properly targets new button keys")
    else:
        print("\n⚠️  Some issues remain - check the details above")
    
    print("\n📋 KEY SEPARATION STRATEGY:")
    print("   • Top Navigation: top_nav_* (Analytics, Logout, Theme)")
    print("   • Menu Navigation: nav_* (Dashboard, Market, Portfolio, etc.)")
    print("   • No conflicts between the two systems")
    
    print("\n🇮🇳 Ready for your Indian Stock Market Dashboard! ✨")