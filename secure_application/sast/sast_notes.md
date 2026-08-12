# SAST Analysis Notes

## Application

Hospital Management System

## Purpose

This directory contains information and results related to Static Application Security Testing (SAST).

The current Lab Assignment 3 version intentionally contains three vulnerabilities:

1. SQL Injection
2. Broken Access Control / Missing Authorization
3. Path Traversal

## Source Code to Analyze

The main source files are:

```text
src/auth.py
src/patients.py
src/medical_records.py