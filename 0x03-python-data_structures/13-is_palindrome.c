#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 *is_palindrome - for holberton school
 *@head: jkjkj
 *Return: from zero to hero
 */
int is_palindrome(listint_t **head)
{
	int a = 0;
	int b = 0;
	listint_t *temp = *head;

	if (*head == NULL)
		return (1);
	while (temp->next != NULL)
	{
		temp = temp->next;
		b++;
	}
	b = b + 1;
	temp = *head;
	while (b > 0)
	{
		while (a != a - 1)
		{
			a++;
			temp = temp->next;
		}
		a = 0;
		if ((*head)->n != temp->n)
		{
			return (0);
		}
		*head = (*head)->next;
		temp = (*head);
		b = b - 2;
	}
	return (1);
}
